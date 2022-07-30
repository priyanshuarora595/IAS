from django.contrib import admin
from .models import Items
from import_export.admin import ImportExportModelAdmin
from .models import Items
# from .resources import ItemResources

# Register your models here.

# admin.site.register(Items)
# @admin.register(Items)
# class ItemsAdmin(ImportExportModelAdmin):
#     list_display = ['item_name','fund_name','LP_NO']
#     # import_list = ['Product_sr_no','item_name','year_of_purchase','fund_name','LP_NO','initial_price','issued_to','Depriciated_Price','Remarks']
#     resource_class = ItemResources