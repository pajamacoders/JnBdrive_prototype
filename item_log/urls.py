from django.urls import path

from . import views
from .view_lake.motor_view import *
from .view_lake.break_view import *
from .view_lake.reducer_view import *
from .view_lake.safety_device_view import *
from .view_lake.parts_type_view import *
from .view_lake.modeltype_view import *
from .view_lake.production_company_view import *
from .view_lake.check_company_view import *
from .view_lake.check_history_view import *
from .view_lake.fault_history_view import *
from .view_lake.contract_view import *
from .view_lake.product_view import *
from .view_lake.user_view import *
app_name = 'item_log'
urlpatterns=[
    path('login/', views.SearchSystemLoginView.as_view(template_name='item_log/login.html'), name='user_login'),
    path('logout/', views.SearchSystemLogoutView.as_view(template_name='item_log/login.html'), name='user_logout'),
    path('search/', views.ProductSearchView.as_view(),name='product_search'),
    path('admin/', views.AdminPageView.as_view(), name='dashboard'),
    #motor
    path('admin/parts/motors/lists', MotorIndexView.as_view(), name='motor_list'),
    path('admin/motor/create', MotorCreateView.as_view(), name='motor_create'),
    path('admin/motor/<str:motor_id>/detail', MotorView.as_view(), name='motor_detail_view'),
    path('admin/motor/<str:motor_id>/delete', MotorDeleteView.as_view(), name='motor_delete_view'),
    #break
    path('admin/parts/breaks/lists', BreakIndexView.as_view(), name='break_list'),
    path('admin/break/create', BreakCreateView.as_view(), name='break_create'),
    path('admin/break/<str:break_id>/detail',BreakView.as_view(), name='break_detail_view'),
    path('admin/break/<str:break_id>/delete', BreakDeleteView.as_view(), name='break_delete_view'),
    #reducer
    path('admin/parts/reducers/lists', ReducerIndexView.as_view(), name='reducer_list'),
    path('admin/reducer/create', ReducerCreateView.as_view(), name='reducer_create'),
    path('admin/reducer/<str:reducer_id>/detail', ReducerView.as_view(), name='reducer_detail_view'),
    path('admin/reducer/<str:reducer_id>/delete', ReducerDeleteView.as_view(), name='reducer_delete_view'),
    # path('parts/add/', parts_view.PartsCreateView.as_view(),name='partscreateview'),
    #safety device
    path('admin/parts/safety_devices/lists', SafetyDeviceIndexView.as_view(), name='safety_device_list'),
    path('admin/safety_device/create', SafetyDeviceCreateView.as_view(), name='safety_device_create'),
    path('admin/safety_device/<str:safety_device_id>/detail', SafetyDeviceView.as_view(), name='safety_device_detail_view'),
    path('admin/safety_device/<str:safety_device_id>/delete', SafetyDeviceDeleteView.as_view(), name='safety_device_delete_view'),
    #parts type
    path('admin/parts/parts_types/lists', PartsTypeIndexView.as_view(), name='parts_type_list'),
    path('admin/parts_type/create', PartsTypeCreateView.as_view(), name='parts_type_create'),
    path('admin/parts_type/<str:name>/detail', PartsTypeView.as_view(), name='parts_type_detail_view'),
    path('admin/parts_type/<str:name>/delete', PartsTypeDeleteView.as_view(), name='parts_type_delete_view'),
    #model type
    path('admin/parts/model_types/lists', ModelTypeIndexView.as_view(), name='model_type_list'),
    path('admin/model_type/create', ModelTypeCreateView.as_view(), name='model_type_create'),
    path('admin/model_type/<str:model>/detail', ModelTypeView.as_view(), name='model_type_detail_view'),
    path('admin/model_type/<str:model>/delete', ModelTypeDeleteView.as_view(), name='model_type_delete_view'),
    # production company
    path('admin/parts/production_companies/lists', ProductionCompanyIndexView.as_view(), name='production_company_list'),
    path('admin/production_company/create', ProductionCompanyCreateView.as_view(), name='production_company_create'),
    path('admin/production_company/<str:business_number>/detail', ProductionCompanyView.as_view(), name='production_company_detail_view'),
    path('admin/production_company/<str:business_number>/delete', ProductionCompanyDeleteView.as_view(), name='production_company_delete_view'),
    #check company
    path('admin/parts/check_companies/lists', CheckCompanyIndexView.as_view(), name='check_company_list'),
    path('admin/check_company/create', CheckCompanyCreateView.as_view(), name='check_company_create'),
    path('admin/check_company/<int:id>/detail', CheckCompanyView.as_view(), name='check_company_detail_view'),
    path('admin/check_company/<int:id>/delete', CheckCompanyDeleteView.as_view(), name='check_company_delete_view'),
    #check history
    path('admin/parts/check_histories/lists', CheckHistoryIndexView.as_view(), name='check_history_list'),
    path('admin/check_history/create', CheckHistoryCreateView.as_view(), name='check_history_create'),
    path('admin/check_history/<int:id>/detail', CheckHistoryView.as_view(), name='check_history_detail_view'),
    path('admin/check_history/<int:id>/delete', CheckHistoryDeleteView.as_view(), name='check_history_delete_view'),
    #fault history
    path('admin/parts/fault_histories/lists', FaultHistoryIndexView.as_view(), name='fault_history_list'),
    path('admin/fault_history/create', FaultHistoryCreateView.as_view(), name='fault_history_create'),
    path('admin/fault_history/<int:id>/detail', FaultHistoryView.as_view(), name='fault_history_detail_view'),
    path('admin/fault_history/<int:id>/delete', FaultHistoryDeleteView.as_view(), name='fault_history_delete_view'),
    #contract
    path('admin/parts/contracts/lists', ContractIndexView.as_view(), name='contract_list'),
    path('admin/contract/create', ContractCreateView.as_view(), name='contract_create'),
    path('admin/contract/<int:id>/detail', ContractView.as_view(), name='contract_detail_view'),
    path('admin/contract/<int:id>/delete', ContractDeleteView.as_view(), name='contract_delete_view'),
    #product
    path('admin/parts/product/lists', ProductIndexView.as_view(), name='product_list'),
    path('admin/product/create', ProductCreateView.as_view(), name='product_create'),
    path('admin/product/<str:serial>/detail', ProductView.as_view(), name='product_detail_view'),
    path('admin/product/<str:serial>/delete', ProductDeleteView.as_view(), name='product_delete_view'),

    #product
    path('admin/user/lists', UserIndexView.as_view(), name='user_list'),
    path('admin/user/create', UserCreateView.as_view(), name='user_create'),
    path('admin/user/<int:id>/detail', UserView.as_view(), name='user_detail_view'),
    path('admin/user/<int:id>/delete', UserDeleteView.as_view(), name='user_delete_view'),
    ]