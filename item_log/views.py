
# Create your views here.

# from django.http import HttpResponse, Http404
# from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from config import settings
from .models import PartsType, Parts, ModelType, Product, Contract, FaultHistory, CheckHistory
from item_log.view_lake.authority_test  import AuthorityTestMixin
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json
from datetime import date, timedelta

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

        if delta<1:
            today = today.replace(month=12+delta).replace(year=today.year-1)
        elif delta>12:
            today = today.replace(month=delta-12).replace(year=today.year+1)
        else:
            today = today.replace(month=delta)
        return today

    def get_upcoming_check_event(self)->list:
        today = date.today()
        start_month = self.update_date(today, -3).replace(day=1)
        last_month = self.update_date(today, 10).replace(day=1)-timedelta(days=1)
        check_events = CheckHistory.objects.exclude(date__isnull=True)
        [obj.__setattr__('end_date',self.update_date(obj.date, obj.effective_duration)) for obj in check_events]
        interest_events = [obj for obj in check_events if obj.end_date >=start_month and obj.end_date<=last_month]
        [obj.__setattr__('site_name', obj.product.contract_set.all()[0].site_name) for obj in interest_events]
        # check_events[0].product.contract_set.all()[0].site_name
        return interest_events

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
    # redirect_field_name = 'next'
    next_page='/search/'
    # def get_default_redirect_url(self):
    #     if self.redirect_field_name:
    #         return self.get_redirect_url(self.next)
    #     else:
    #         return self.get_default_redirect_url(self)

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

class ProductInfo(View):
    initial = {'key': 'value'}
    template_name = 'ProductInfoView.html'

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

