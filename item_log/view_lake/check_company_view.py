from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import CheckCompany
from item_log.form_lake.check_company_form import CheckCompanyUpdateForm

class CheckCompanyIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'adminpage/check_company_index.html'
    model = CheckCompany
    paginate_by = 20
    context_object_name = 'check_companies'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class CheckCompanyDetailView(LoginRequiredMixin, generic.DetailView):
    pk_url_kwarg='id'
    model = CheckCompany
    template_name = 'adminpage/check_company_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CheckCompanyUpdateForm(instance=self.model.objects.get(pk=self.kwargs['id']))
        return context


class CheckCompanyUpdateFormView(LoginRequiredMixin, UpdateView):
    template_name = 'adminpage/check_company_detail_view.html'
    form_class = CheckCompanyUpdateForm
    model = CheckCompany
    pk_url_kwarg='id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CheckCompanyView(View):

    def get(self, request, *args, **kwargs):
        view = CheckCompanyDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CheckCompanyUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class CheckCompanyCreateView(LoginRequiredMixin, CreateView):
    model = CheckCompany
    fields = '__all__'
    template_name = 'adminpage/check_company_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CheckCompanyUpdateForm()
        return context

class CheckCompanyDeleteView(LoginRequiredMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='id'
    model = CheckCompany
    success_url = reverse_lazy('item_log:check_company_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)