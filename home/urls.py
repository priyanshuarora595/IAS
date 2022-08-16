from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
    path('del_user',views.del_profile,name='del_profile'),
    path('del_item',views.del_item,name='del_item'),
    path('del_fund',views.del_fund,name='del_fund'),
    path('add_item',views.add_item,name='add_item'),
    path('add_funds',views.add_funds,name='add_funds'),
    path('all_entries',views.all_entries,name='all_entries'),
    path('all_funds',views.all_funds,name='all_funds'),
    path('edit_entry/<str:it_id>/',views.edit_entry,name='edit_entry'),
    path("edit_fund/<str:it_id>/",views.edit_fund,name='edit_fund'),
    path("fund_date/<str:it_id>/",views.fund_date,name='fund_date'),
    path('edit_entry_submit',views.edit_entry_submit,name='edit_entry_submit'),
    path('edit_fund_submit',views.edit_fund_submit,name='edit_fund_submit'),
    path('simple_upload',views.simple_upload,name='simple_upload'),
    path('export_xlsx',views.export_xlsx,name='export_xlsx'),
    path('export_xls',views.export_xls,name='export_xls'),
    path('export_csv',views.export_csv,name='export_csv'),
    path('scan_barcode',views.scan_barcode,name='scan_barcode'),
    path('filter_data',views.filter_data,name='filter_data'),
]
