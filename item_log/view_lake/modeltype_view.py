from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import ModelType
from item_log.form_lake.modeltype_form import ModelTypeUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class ModelTypeIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/model_type_index.html'
    model = ModelType
    paginate_by = 20
    context_object_name = 'model_types'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class ModelTypeDetailView(LoginRequiredMixin, AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='model'
    model = ModelType
    template_name = 'adminpage/model_type_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ModelTypeUpdateForm(instance=self.model.objects.get(pk=self.kwargs['model']))
        return context


class ModelTypeUpdateFormView(LoginRequiredMixin, AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/model_type_detail_view.html'
    form_class = ModelTypeUpdateForm
    model = ModelType
    pk_url_kwarg='model'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ModelTypeView(View):

    def get(self, request, *args, **kwargs):
        view = ModelTypeDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ModelTypeUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class ModelTypeCreateView(LoginRequiredMixin, AuthorityTestMixin, CreateView):
    model = ModelType
    form_class = ModelTypeUpdateForm
    template_name = 'adminpage/model_type_create_view.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ModelTypeUpdateForm()
    #     return context

class ModelTypeDeleteView(LoginRequiredMixin, AuthorityTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='model'
    model = ModelType
    success_url = reverse_lazy('item_log:model_type_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)