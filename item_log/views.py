
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
from item_log.view_lake.authority_test  import AuthorityTestMixin
# from .models import Item, Buyer, SalesHistory, InspectionLog


class AdminPageView(LoginRequiredMixin, AuthorityTestMixin, TemplateView):
    login_url = settings.LOGIN_URL
    template_name = 'adminpage/layout-static.html'

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

