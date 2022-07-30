from import_export import  widgets,fields,resources
from .models import Items , Funds
from import_export.widgets import ForeignKeyWidget



# class ForeignkeyRequiredWidget(widgets.ForeignKeyWidget):
#      def clean(self, value,field='fund_name',row=None, *args, **kwargs):
#             if value:
#                 print(self.field, value)
#                 return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: value})
#             else:
#                 raise ValueError(self.field+ " required")



# class ItemResources(resources.ModelResource):
#     fund_name = fields.Field(column_name='fund_name',attribute='fund_name', widget=widgets.ForeignKeyWidget(Funds,field='fund_name'))
#     class Meta:
#         model = Items
#         export_order = ['Product_sr_no','item_name','year_of_purchase','fund_name','LP_NO','initial_price',	'issued_to'	,'Depreciated_Price','Remarks','barcode']
#         field = 'fund_name'
#         clean_model_instances = True
        
    # def dehydrate_fund_name(self, item):
    #     print(item.fund_name.fund_name)
    #     return item.fund_name.fund_name # You can get all fields of related model. This is example.


class ItemResources(resources.ModelResource):
    
    fund_name = fields.Field(column_name='fund_name',attribute='fund_name', widget=ForeignKeyWidget(Funds,field='fund_name'))
    class Meta:
        model = Items
        # fields=('fund_name',)
        export_order = ['Product_sr_no','item_name','year_of_purchase','fund_name','LP_NO','initial_price','issued_to','Depreciated_Price','Remarks','barcode']
        import_id_fields = ['Product_sr_no']
        
  