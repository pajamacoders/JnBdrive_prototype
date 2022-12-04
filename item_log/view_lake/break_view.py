from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Break
from item_log.form_lake.break_form import BreakUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin

class BreakIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/break_index.html'
    model = Break
    paginate_by = 20
    context_object_name = 'breaks'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class BreakDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='break_id'
    model = Break
    template_name = 'adminpage/break_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BreakUpdateForm(instance=self.model.objects.get(pk=self.kwargs['break_id']))
        return context


class BreakUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/break_detail_view.html'
    form_class = BreakUpdateForm
    model = Break
    pk_url_kwarg='break_id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class BreakView(View):

    def get(self, request, *args, **kwargs):
        view = BreakDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = BreakUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class BreakCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = Break
    fields = '__all__'
    template_name = 'adminpage/break_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BreakUpdateForm()
        return context

class BreakDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='break_id'
    model = Break
    success_url = reverse_lazy('item_log:break_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)