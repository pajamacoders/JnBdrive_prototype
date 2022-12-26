
# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.base import TemplateView
from config import settings
from .models import PartsType, Parts, ModelType, Product, Contract, FaultHistory, CheckHistory
from item_log.view_lake.authority_test  import AuthorityTestMixin
from django.db.models import Count
import json
from datetime import date, timedelta
import calendar

# from .models import Item, Buyer, SalesHistory, InspectionLog


class AdminPageView(LoginRequiredMixin, AuthorityTestMixin, TemplateView):
    login_url = settings.LOGIN_URL
    template_name = 'adminpage/barchart.html'

    def get_parts_statics(self)-> list:
        part_type = PartsType.objects.all()
        data=[]
        for i in range(part_type.count()):
            tmp={'type':part_type[i].name}
            tmp.update(part_type[i].parts_set.aggregate(count=Count('*')))
            data.append(tmp)
        return data
    
    def get_model_statics(self)->list:
        model_type = ModelType.objects.all()
        data=[]
        for i in range(model_type.count()):
            tmp={'type':model_type[i].model}
            tmp.update(model_type[i].product_set.aggregate(count=Count('*')))
            data.append(tmp)
        return data
    
    def update_date(self, today, month):
        """
        the input month range from -12 ~ 12
        """
        delta = today.month +month
        if delta == 0:
            yoffset=-1
            month=12
        elif delta==12:
            yoffset=0
            month=12
        else:
            yoffset, month = delta//12, delta%12
            month = month if month else 12
        try:
            lastday=calendar.monthrange(today.year+yoffset, month)[1]
        except:
            print(month)
        date = today.replace(year=today.year+yoffset, month=month, day=lastday) \
            if today.day>=lastday else today.replace(year=today.year+yoffset, month=month)
        return date

    def get_upcoming_check_event(self)->list:
        today = date.today()
        start_month = self.update_date(today, -3).replace(day=1)
        last_month = self.update_date(today, 10).replace(day=1)-timedelta(days=1)
        check_events = CheckHistory.objects.exclude(date__isnull=True)
        [obj.__setattr__('end_date',self.update_date(obj.date, obj.effective_duration)) for obj in check_events]
        interest_events_products = [obj for obj in check_events if obj.end_date >=start_month and obj.end_date<=last_month and obj.product and obj.product.contract_set.aggregate(count=Count('*'))['count']]
        interest_events_parts = [obj for obj in check_events if obj.end_date >=start_month and obj.end_date<=last_month and obj.part and obj.part.contract_set.aggregate(count=Count('*'))['count']]
        try:
            [obj.__setattr__('site_name', obj.product.contract_set.all()[0].site_name) for obj in interest_events_products]
            [obj.__setattr__('site_name', obj.part.contract_set.all()[0].site_name) for obj in interest_events_parts]
        except: 
            print(interest_events_parts)
        # check_events[0].product.contract_set.all()[0].site_name
        return interest_events_products+interest_events_parts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parts_statics = self.get_parts_statics()  
        context['parts_statics'] = json.dumps(parts_statics)
        model_statics = self.get_model_statics()
        context['model_statics'] = json.dumps(model_statics)
        context['upcoming_check']=self.get_upcoming_check_event()
        return context

# class AdminPageLoginView(LoginView):
#     next_page = '/admin/'
    
class AdminPageLogoutView(LogoutView):
    pass

class SearchSystemLogoutView(LogoutView):
    next_page='/login/'
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)
class SearchSystemLoginView(LoginView):
    next_page='/search/'
    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        return context

class ProductSearchView(LoginRequiredMixin,TemplateView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'next'
    template_name = 'item_log/searchview_v2.html'
    # paginate_by = 20

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        required_serial = self.request.GET.get('serial')
        if required_serial:
            products = Product.objects.filter(serial__icontains=required_serial)
            if products:
                context['products']=products
            else:
                parts = Parts.objects.filter(serial__icontains=required_serial)
                if parts:
                    context['parts']=parts
        return context

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)  
        return context
        
    
    def post(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        return context

class ComprehensiveInfoView(LoginRequiredMixin, generic.DetailView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'next'
    template_name = 'item_log/ProductInfoView.html'
    pk_url_kwarg='serial'
    model=Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contracts=context['product'].contract_set.order_by('-installation_date')
        context['contract']=None
        if contracts:
            context['contract']=contracts[0]
        context['modelType']=context['product'].model
        context['production_company']=context['product'].production_company
        context['checkhistories'] = context['product'].checkhistory_set.order_by('-date')
        [obj.__setattr__('end_date',self.update_date(obj.date, obj.effective_duration)) for obj in context['checkhistories']]
        
        context['latest_check_date']='-'
        if len(context['checkhistories']):
            context['latest_check_date'] = context['checkhistories'][0].date
            context['next_check_date'] = context['checkhistories'][0].end_date
            context['final_check_company'] = context['checkhistories'][0].inspection_agency.name
        
        motor_faults=FaultHistory.objects.filter(parts=context['product'].motor_id).order_by('-date')
        brake_faults=FaultHistory.objects.filter(parts=context['product'].brake_id).order_by('-date')
        reduce_faults=FaultHistory.objects.filter(parts=context['product'].reducer_id).order_by('-date')
        safety_device_faults=FaultHistory.objects.filter(parts=context['product'].safety_device_id).order_by('-date')
        context['fault_histories'] = motor_faults|brake_faults|reduce_faults|safety_device_faults
        # context['form'] = BreakUpdateForm(instance=self.model.objects.get(pk=self.kwargs['break_id']))
        return context

    def update_date(self, today, month):
        """
        the input month range from -12 ~ 12
        """
        delta = today.month +month
        if delta == 0:
            yoffset=-1
            month=12
        elif delta==12:
            yoffset=0
            month=12
        else:
            yoffset, month = delta//12, delta%12
            month = month if month else 12
        try:
            lastday=calendar.monthrange(today.year+yoffset, month)[1]
        except:
            print(month)
        date = today.replace(year=today.year+yoffset, month=month, day=lastday) \
            if today.day>=lastday else today.replace(year=today.year+yoffset, month=month)
        return date

    def get_upcoming_check_event(self)->list:
        today = date.today()
        start_month = self.update_date(today, -3).replace(day=1)
        last_month = self.update_date(today, 10).replace(day=1)-timedelta(days=1)
        check_events = CheckHistory.objects.exclude(date__isnull=True)
        [obj.__setattr__('end_date',self.update_date(obj.date, obj.effective_duration)) for obj in check_events]
        interest_events = [obj for obj in check_events if obj.end_date >=start_month and obj.end_date<=last_month and obj.product]
        [obj.__setattr__('site_name', obj.product.contract_set.all()[0].site_name) for obj in interest_events]
        # check_events[0].product.contract_set.all()[0].site_name
        return interest_events


    


