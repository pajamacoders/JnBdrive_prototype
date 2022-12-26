from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import PartsType
from item_log.form_lake.parts_type_form import PartsTypeUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class PartsTypeIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/parts_type_index.html'
    model = PartsType
    # paginate_by = 20
    context_object_name = 'parts_types'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class PartsTypeDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='name'
    model = PartsType
    template_name = 'adminpage/parts_type_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PartsTypeUpdateForm(instance=self.model.objects.get(pk=self.kwargs['name']))
        return context


class PartsTypeUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/parts_type_detail_view.html'
    form_class = PartsTypeUpdateForm
    model = PartsType
    pk_url_kwarg='name'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PartsTypeView(View):

    def get(self, request, *args, **kwargs):
        view = PartsTypeDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PartsTypeUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class PartsTypeCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = PartsType
    fields = '__all__'
    template_name = 'adminpage/parts_type_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PartsTypeUpdateForm()
        return context

class PartsTypeDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='name'
    model = PartsType
    success_url = reverse_lazy('item_log:parts_type_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)