from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from item_log.form_lake.parts_form import PartsCreateForm

class PartsCreateView_old(View):
    form_class = PartsCreateForm
    initial = {'key': 'value'}
    template_name = 'item_log/partscreateview.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'sabi_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/item_log/parts/add/')

        return render(request, self.template_name, {'sabi_form': form})

class PartsCreateView(View):
    form_class = PartsCreateForm
    initial = {'key': 'value'}
    template_name = 'item_log/partscreateview.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'sabi_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/item_log/parts/add/')

        return render(request, self.template_name, {'sabi_form': form})

# class PartsUpdateView(UpdateView):
#     model = Parts
#     fields = ['serial']
# class PartsDeleteView(DeleteView):
#     model = Parts
#     fields = ['serial']