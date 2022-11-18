from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Contract
from item_log.form_lake.contract_form import ContractUpdateForm

class ContractIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'adminpage/contract_index.html'
    model = Contract
    paginate_by = 20
    context_object_name = 'contracts'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class ContractDetailView(LoginRequiredMixin, generic.DetailView):
    pk_url_kwarg='id'
    model = Contract
    template_name = 'adminpage/contract_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContractUpdateForm(instance=self.model.objects.get(pk=self.kwargs['id']))
        return context


class ContractUpdateFormView(LoginRequiredMixin, UpdateView):
    template_name = 'adminpage/contract_detail_view.html'
    form_class = ContractUpdateForm
    model = Contract
    pk_url_kwarg='id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ContractView(View):

    def get(self, request, *args, **kwargs):
        view = ContractDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ContractUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    fields = '__all__'
    template_name = 'adminpage/contract_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContractUpdateForm()
        return context

class ContractDeleteView(LoginRequiredMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='id'
    model = Contract
    success_url = reverse_lazy('item_log:contract_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)