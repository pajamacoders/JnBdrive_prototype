from django.urls import path

from . import views
from .view_lake import parts_view 
app_name = 'item_log'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('parts/add/', parts_view.PartsCreateView.as_view(),name='partscreateview'),
    # ex: /polls/5/results/
    path('<str:item_id>/brief_inspection_history/', views.brief_inspection_history, name='brief_inspection_history'),
    # ex: /polls/5/vote/
    path('<str:item_id>/<str:inspection_date>/detailed_inspection_history/', views.detailed_inspection_history, name='detailed_inspection_history'),
    path('<str:item_id>/saleshistory/', views.saleshistory, name='saleshistory'),

    ]