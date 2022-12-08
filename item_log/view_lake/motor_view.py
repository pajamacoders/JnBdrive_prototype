from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Motor
from item_log.form_lake.motor_form import MotorUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class MotorIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/motor_index.html'
    model = Motor
    paginate_by = 20
    context_object_name = 'motors'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class MotorDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='motor_id'
    model = Motor
    template_name = 'adminpage/motor_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MotorUpdateForm(instance=self.model.objects.get(pk=self.kwargs['motor_id']))
        return context


class MotorUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/motor_detail_view.html'
    form_class = MotorUpdateForm
    model = Motor
    pk_url_kwarg='motor_id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MotorView(View):

    def get(self, request, *args, **kwargs):
        view = MotorDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = MotorUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class MotorCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = Motor
    template_name = 'adminpage/motor_create_view.html'
    form_class = MotorUpdateForm


class MotorDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    pk_url_kwarg='motor_id'
    model = Motor
    success_url = reverse_lazy('item_log:motor_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)