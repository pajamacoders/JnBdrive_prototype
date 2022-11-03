from django.urls import path

from . import views
from .view_lake import parts_view, motor_view
app_name = 'item_log'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.SearchSystemLoginView.as_view(template_name='item_log/login.html'), name='user_login'),
    path('logout/', views.SearchSystemLogoutView.as_view(template_name='item_log/login.html'), name='user_logout'),
    path('search/', views.ProductSearchView.as_view(),name='product_search'),
    path('admin/', views.AdminPageView.as_view(), name='dashboard'),
    path('admin/parts/motors/lists', motor_view.MotorIndexView.as_view(), name='motor_list'),
    path('admin/motor/create', motor_view.MotorCreateView.as_view(), name='motor_create'),
    path('admin/motor/<str:motor_id>/detail', motor_view.MotorView.as_view(), name='motor_detail_view'),
    path('admin/motor/<str:motor_id>/delete', motor_view.MotorDeleteView.as_view(), name='motor_delete_view'),
    path('parts/add/', parts_view.PartsCreateView.as_view(),name='partscreateview'),
    path('<str:item_id>/datails/', views.ProductInfo.as_view(), name='ProductInfo'),
    path('<str:item_id>/<str:inspection_date>/detailed_inspection_history/', views.detailed_inspection_history, name='detailed_inspection_history'),
    path('<str:item_id>/saleshistory/', views.saleshistory, name='saleshistory'),
    
    ]