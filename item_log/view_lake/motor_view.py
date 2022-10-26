
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from config import settings
from item_log.models import Parts, Motor

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
class MotorDetailView(LoginRequiredMixin, generic.DetailView):
    pass

class MotorAddView(LoginRequiredMixin, ):
    pass

class MotorChangeView(LoginRequiredMixin):
    pass