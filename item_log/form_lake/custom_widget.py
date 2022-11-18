from django import forms
from django.utils.html import html_safe

@html_safe
class Select2JSPath:
    def __str__(self):
        return '<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js">'

@html_safe
class Select2CSSPath:
    def __str__(self):
        return '<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />'


@html_safe
class JQuery:
    def __str__(self):
        return '<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js">'



class AutoCompleteWidget(forms.Select):
    template_name = 'widgets/autocomplete_select.html'

    class Media:
        css = {
            'all' : [
                Select2CSSPath(),#"//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/css/select2.min.css",
            ],
        }
        js = [
            JQuery(),
            Select2JSPath(), #"//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/js/select2.min.js",
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs)
        context['style'] = 'min-width:200px;'
        return context