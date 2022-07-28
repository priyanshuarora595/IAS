from django.contrib import admin
from .models import Items
from import_export.admin import ImportExportActionModelAdmin
from .models import Items

# Register your models here.

# admin.site.register(Items)
@admin.register(Items)
class ItemsAdmin(ImportExportActionModelAdmin):
    list_display = ('item_name','fund_name','LP_NO')
    ['Product_sr_no','item_name','year_of_purchase','fund_name','LP_NO','initial_price','issued_to','Depriciated_Price','Remarks']