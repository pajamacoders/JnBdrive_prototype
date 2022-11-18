from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import FaultHistory
from item_log.form_lake.fault_history_form import FaultHistoryUpdateForm

class FaultHistoryIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'adminpage/fault_history_index.html'
    model = FaultHistory
    paginate_by = 20
    context_object_name = 'fault_histories'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class FaultHistoryDetailView(LoginRequiredMixin, generic.DetailView):
    pk_url_kwarg='id'
    model = FaultHistory
    template_name = 'adminpage/fault_history_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FaultHistoryUpdateForm(instance=self.model.objects.get(pk=self.kwargs['id']))
        return context


class FaultHistoryUpdateFormView(LoginRequiredMixin, UpdateView):
    template_name = 'adminpage/fault_history_detail_view.html'
    form_class = FaultHistoryUpdateForm
    model = FaultHistory
    pk_url_kwarg='id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class FaultHistoryView(View):

    def get(self, request, *args, **kwargs):
        view = FaultHistoryDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = FaultHistoryUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class FaultHistoryCreateView(LoginRequiredMixin, CreateView):
    model = FaultHistory
    fields = '__all__'
    template_name = 'adminpage/fault_history_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FaultHistoryUpdateForm()
        return context



class FaultHistoryDeleteView(LoginRequiredMixin, DeleteView):
    pk_url_kwarg='id'
    model = FaultHistory
    success_url = reverse_lazy('item_log:fault_history_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)