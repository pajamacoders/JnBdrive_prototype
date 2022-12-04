from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import SafetyDevice
from item_log.form_lake.safety_device_form import SafetyDeviceUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class SafetyDeviceIndexView(LoginRequiredMixin,  AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/safety_device_index.html'
    model = SafetyDevice
    paginate_by = 20
    context_object_name = 'safety_devices'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class SafetyDeviceDetailView(LoginRequiredMixin,  AuthorityTestMixin,  generic.DetailView):
    pk_url_kwarg='safety_device_id'
    model = SafetyDevice
    template_name = 'adminpage/safety_device_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SafetyDeviceUpdateForm(instance=self.model.objects.get(pk=self.kwargs['safety_device_id']))
        return context


class SafetyDeviceUpdateFormView(LoginRequiredMixin, AuthorityTestMixin,  UpdateView):
    template_name = 'adminpage/safety_device_detail_view.html'
    form_class = SafetyDeviceUpdateForm
    model = SafetyDevice
    pk_url_kwarg='safety_device_id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class SafetyDeviceView(View):

    def get(self, request, *args, **kwargs):
        view = SafetyDeviceDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SafetyDeviceUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class SafetyDeviceCreateView(LoginRequiredMixin, AuthorityTestMixin,  CreateView):
    model = SafetyDevice
    fields = '__all__'
    template_name = 'adminpage/safety_device_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SafetyDeviceUpdateForm()
        return context

class SafetyDeviceDeleteView(LoginRequiredMixin,  AuthorityTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='safety_device_id'
    model = SafetyDevice
    success_url = reverse_lazy('item_log:safety_device_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)