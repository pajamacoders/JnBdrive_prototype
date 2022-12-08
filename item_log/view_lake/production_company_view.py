from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import ProductionCompany
from item_log.form_lake.production_company_form import ProductionCompanyUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class ProductionCompanyIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/production_company_index.html'
    model = ProductionCompany
    paginate_by = 20
    context_object_name = 'production_companies'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class ProductionCompanyDetailView(LoginRequiredMixin, AuthorityTestMixin,  generic.DetailView):
    pk_url_kwarg='business_number'
    model = ProductionCompany
    template_name = 'adminpage/production_company_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductionCompanyUpdateForm(instance=self.model.objects.get(pk=self.kwargs['business_number']))
        return context


class ProductionCompanyUpdateFormView(LoginRequiredMixin, AuthorityTestMixin,  UpdateView):
    template_name = 'adminpage/production_company_detail_view.html'
    form_class = ProductionCompanyUpdateForm
    model = ProductionCompany
    pk_url_kwarg='business_number'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductionCompanyView(View):

    def get(self, request, *args, **kwargs):
        view = ProductionCompanyDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProductionCompanyUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class ProductionCompanyCreateView(LoginRequiredMixin,  AuthorityTestMixin, CreateView):
    model = ProductionCompany
    form_class = ProductionCompanyUpdateForm
    template_name = 'adminpage/production_company_create_view.html'



class ProductionCompanyDeleteView(LoginRequiredMixin, AuthorityTestMixin,  DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='business_number'
    model = ProductionCompany
    success_url = reverse_lazy('item_log:production_company_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)