from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from item_log.form_lake.user_creation_form import UserCreationFormWrap
from item_log.view_lake.authority_test  import SuperUserTestMixin
class UserIndexView(LoginRequiredMixin, SuperUserTestMixin, generic.ListView):
    template_name = 'adminpage/user_index.html'
    model = User
    # paginate_by = 20
    context_object_name = 'users'
    ordering = ['username']
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> dict:
        # return Poll.active.filter(user=self.request.user).order_by('-pub_date')[:5]
        query_set = super().get_queryset()
        return query_set

class UserDetailView(LoginRequiredMixin, SuperUserTestMixin, generic.DetailView):
    pk_url_kwarg='id'
    model = User
    template_name = 'adminpage/user_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationFormWrap(instance=self.model.objects.get(pk=self.kwargs['id']))
        return context


class UserUpdateView(LoginRequiredMixin, SuperUserTestMixin, UpdateView):
    template_name = 'adminpage/user_detail_view.html'
    form_class = UserCreationFormWrap
    model = User
    pk_url_kwarg='id'
    success_url=reverse_lazy('item_log:user_list')
    def post(self, request, *args, **kwargs):
      
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserView(View):

    def get(self, request, *args, **kwargs):
        view = UserDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UserUpdateView.as_view()
        return view(request, *args, **kwargs)

class UserCreateView(LoginRequiredMixin, SuperUserTestMixin, generic.FormView):

    template_name = 'adminpage/user_create_view.html'
    success_url=reverse_lazy('item_log:user_list')
    form_class=UserCreationFormWrap
    # model=User
    # fields=['username', 'password', 'first_name', 'last_name', 'email', 'is_staff']
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = UserCreationFormWrap()
    #     return context
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)
    # def get_success_url(self):
    #     return reverse('user_list', kwargs={'pk': self.object.pk})

class UserDeleteView(LoginRequiredMixin, SuperUserTestMixin, DeleteView):
    # template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='id'
    model = User
    success_url = reverse_lazy('item_log:user_list')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return self.delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)