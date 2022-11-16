from django.urls import path

from . import views
from .view_lake import parts_view, motor_view, break_view, reducer_view

app_name = 'item_log'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.SearchSystemLoginView.as_view(template_name='item_log/login.html'), name='user_login'),
    path('logout/', views.SearchSystemLogoutView.as_view(template_name='item_log/login.html'), name='user_logout'),
    path('search/', views.ProductSearchView.as_view(),name='product_search'),
    path('admin/', views.AdminPageView.as_view(), name='dashboard'),
    #motor
    path('admin/parts/motors/lists', motor_view.MotorIndexView.as_view(), name='motor_list'),
    path('admin/motor/create', motor_view.MotorCreateView.as_view(), name='motor_create'),
    path('admin/motor/<str:motor_id>/detail', motor_view.MotorView.as_view(), name='motor_detail_view'),
    path('admin/motor/<str:motor_id>/delete', motor_view.MotorDeleteView.as_view(), name='motor_delete_view'),
    #break
    path('admin/parts/breaks/lists', break_view.BreakIndexView.as_view(), name='break_list'),
    path('admin/break/create', break_view.BreakCreateView.as_view(), name='break_create'),
    path('admin/break/<str:break_id>/detail', break_view.BreakView.as_view(), name='break_detail_view'),
    path('admin/break/<str:break_id>/delete', break_view.BreakDeleteView.as_view(), name='break_delete_view'),
    #reducer
    path('admin/parts/reducers/lists', reducer_view.ReducerIndexView.as_view(), name='reducer_list'),
    path('admin/reducer/create', reducer_view.ReducerCreateView.as_view(), name='reducer_create'),
    path('admin/reducer/<str:reducer_id>/detail', reducer_view.ReducerView.as_view(), name='reducer_detail_view'),
    path('admin/reducer/<str:reducer_id>/delete', reducer_view.ReducerDeleteView.as_view(), name='reducer_delete_view'),
    # path('parts/add/', parts_view.PartsCreateView.as_view(),name='partscreateview'),
    
    
    ]