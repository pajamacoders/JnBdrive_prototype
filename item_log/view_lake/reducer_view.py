from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Reducer
from item_log.form_lake.reducer_form import ReducerUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class ReducerIndexView(LoginRequiredMixin,  AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/reducer_index.html'
    model = Reducer
    paginate_by = 20
    context_object_name = 'reducers'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class ReducerDetailView(LoginRequiredMixin,  AuthorityTestMixin,  generic.DetailView):
    pk_url_kwarg='reducer_id'
    model = Reducer
    template_name = 'adminpage/reducer_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReducerUpdateForm(instance=self.model.objects.get(pk=self.kwargs['reducer_id']))
        return context


class ReducerUpdateFormView(LoginRequiredMixin,  AuthorityTestMixin,  UpdateView):
    template_name = 'adminpage/reducer_detail_view.html'
    form_class = ReducerUpdateForm
    model = Reducer
    pk_url_kwarg='reducer_id'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ReducerView(View):

    def get(self, request, *args, **kwargs):
        view = ReducerDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReducerUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class ReducerCreateView(LoginRequiredMixin,  AuthorityTestMixin,  CreateView):
    model = Reducer
    form_class = ReducerUpdateForm
    template_name = 'adminpage/reducer_create_view.html'


class ReducerDeleteView(LoginRequiredMixin,  AuthorityTestMixin,  DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='reducer_id'
    model = Reducer
    success_url = reverse_lazy('item_log:reducer_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)