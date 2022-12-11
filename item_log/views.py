
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
            tmp.update(model_type[1].product_set.aggregate(count=Count('*')))
            data.append(tmp)
        return data
    
    def update_date(self, today, month):
        """
        the input month range from -12 ~ 12
        """
        delta = today.month +month
        today.replace(month=12+delta).replace(year=today.year-1)
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
        check_events = CheckHistory.objects.filter(date__gte=start_month, date__lte=last_month)
        ev_per_month  = check_events.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('*')).values('month', 'count')
        pass
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parts_statics = self.get_parts_statics()  
        context['parts_statics'] = json.dumps(parts_statics)
        model_statics = self.get_model_statics()
        context['model_statics'] = json.dumps(model_statics)
        self.get_upcoming_check_event()
        # context['part_inventories']=
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

