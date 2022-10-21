
# Create your views here.

# from django.http import HttpResponse, Http404
# from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from config import settings
from .models import Parts, Motor, Break, Reducer, SafetyDevice
# from .models import Item, Buyer, SalesHistory, InspectionLog

class SaerchSystemLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)
class SearchSystemLoginView(LoginView):
    next_page = '/search/'



class ProductSearchView(LoginRequiredMixin,TemplateView):
    login_url = settings.LOGIN_URL
    redirect_field_name = 'next'
    template_name = 'item_log/searchview_v2.html'


class IndexView(generic.ListView):
    template_name = 'item_log/index.html'
    context_object_name = 'logs'

    def get_queryset(self):
        pass

class ProductInfo(View):
    initial = {'key': 'value'}
    template_name = 'ProductInfoView.html'

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


def brief_inspection_history(request, item_id):
    pass

def detailed_inspection_history(request, item_id, inspection_date):
    pass

def saleshistory(request, item_id):
    pass
