from django import forms
from django.utils import timezone
from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from config import settings
from item_log.models import Parts, Motor, PartsType

class MotorIndexView(LoginRequiredMixin, generic.ListView):
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



class MotorUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs.keys():
            self.fields['serial'].disabled = True
        else:
            self.fields['category'].initial='모터'
    class Meta:
        model = Motor
        fields = ['serial', 'category', 'production_date', 'discard_date', 'model_serial', 'capacity']
        widgets = {
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
        }
class MotorDetailView(LoginRequiredMixin, generic.DetailView):
    pk_url_kwarg='motor_id'
    model = Motor
    template_name = 'adminpage/motor_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MotorUpdateForm(instance=self.model.objects.get(pk=self.kwargs['motor_id']))
        return context


class MotorUpdateFormView(LoginRequiredMixin, UpdateView):
    template_name = 'adminpage/motor_detail_view.html'
    form_class = MotorUpdateForm
    model = Motor
    pk_url_kwarg='motor_id'
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    # def get_success_url(self):
    #     return reverse('item_log:motor_detail_view', kwargs={'motor_id': self.object.pk})

class MotorView(View):

    def get(self, request, *args, **kwargs):
        view = MotorDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = MotorUpdateFormView.as_view()
        return view(request, *args, **kwargs)


class MotorCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=PartsType.objects.all())
    category.initial='모터'
    class Meta:
        model = Motor
        fields = ['serial', 'category', 'production_date', 'discard_date', 'model_serial', 'capacity']
        widgets = {
            'production_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
            'discard_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
        }
class MotorCreateView(LoginRequiredMixin, CreateView):
    model = Motor
    fields = '__all__'
    template_name = 'adminpage/motor_create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MotorUpdateForm()#MotorCreateForm()
        return context


class MotorDeleteView(LoginRequiredMixin, DeleteView):
    template_name="adminpage/motor_delete_view.html"
    pk_url_kwarg='motor_id'
    model = Motor
    success_url = reverse_lazy('item_log:motor_list')
    