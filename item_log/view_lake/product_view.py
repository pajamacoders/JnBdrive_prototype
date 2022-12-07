from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.models import Product
from item_log.form_lake.product_form import ProductUpdateForm
from item_log.view_lake.authority_test  import AuthorityTestMixin
class ProductIndexView(LoginRequiredMixin, AuthorityTestMixin, generic.ListView):
    template_name = 'adminpage/product_index.html'
    model = Product
    paginate_by = 20
    context_object_name = 'products'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class ProductDetailView(LoginRequiredMixin,  AuthorityTestMixin, generic.DetailView):
    pk_url_kwarg='serial'
    model = Product
    template_name = 'adminpage/product_detail_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductUpdateForm(instance=self.model.objects.get(pk=self.kwargs['serial']))
        return context


class ProductUpdateFormView(LoginRequiredMixin,  AuthorityTestMixin, UpdateView):
    template_name = 'adminpage/product_detail_view.html'
    form_class = ProductUpdateForm
    model = Product
    pk_url_kwarg='serial'
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductView(View):

    def get(self, request, *args, **kwargs):
        view = ProductDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProductUpdateFormView.as_view()
        return view(request, *args, **kwargs)

class ProductCreateView(LoginRequiredMixin,  AuthorityTestMixin,  CreateView):
    model = Product
    # fields = '__all__'
    template_name = 'adminpage/product_create_view.html'
    form_class = ProductUpdateForm
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ProductUpdateForm()
    #     return context

class ProductDeleteView(LoginRequiredMixin,  AuthorityTestMixin,  DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='serial'
    model = Product
    success_url = reverse_lazy('item_log:product_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)