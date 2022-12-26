from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Brake
from item_log.form_lake.brake_form import BrakeUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin

class BrakeIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/brake_index.html'
    model = Brake
    context_object_name = 'brakes'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class BrakeDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='brake_id'
    model = Brake
    template_name = 'adminpage/brake_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BrakeUpdateForm(instance=self.model.objects.get(pk=self.kwargs['brake_id']))
        return context


class BrakeUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/brake_detail_view.html'
    form_class = BrakeUpdateForm
    model = Brake
    pk_url_kwarg='brake_id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class BrakeView(View):

    def get(self, request, *args, **kwargs):
        view = BrakeDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = BrakeUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class BrakeCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = Brake
    form_class = BrakeUpdateForm
    template_name = 'adminpage/brake_create_view.html'

class BreakDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='brake_id'
    model = Brake
    success_url = reverse_lazy('item_log:brake_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)