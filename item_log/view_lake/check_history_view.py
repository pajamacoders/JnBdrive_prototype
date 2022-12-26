from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import CheckHistory
from item_log.form_lake.check_history_form import CheckHistoryUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class CheckHistoryIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/check_history_index.html'
    model = CheckHistory
    # paginate_by = 20
    context_object_name = 'check_histories'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class CheckHistoryDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='id'
    model = CheckHistory
    template_name = 'adminpage/check_history_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CheckHistoryUpdateForm(instance=self.model.objects.get(pk=self.kwargs['id']))
        return context


class CheckHistoryUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/check_history_detail_view.html'
    form_class = CheckHistoryUpdateForm
    model = CheckHistory
    pk_url_kwarg='id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CheckHistoryView(View):

    def get(self, request, *args, **kwargs):
        view = CheckHistoryDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CheckHistoryUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class CheckHistoryCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = CheckHistory
    # fields = '__all__'
    template_name = 'adminpage/check_history_create_view.html'
    form_class = CheckHistoryUpdateForm
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CheckHistoryUpdateForm()
    #     return context



class CheckHistoryDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    pk_url_kwarg='id'
    model = CheckHistory
    success_url = reverse_lazy('item_log:check_history_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)