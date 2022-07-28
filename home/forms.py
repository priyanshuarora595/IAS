
from django import forms
from .models import Items
from barcode import EAN13
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class ItemsForm(forms.ModelForm):
    
    # def save_overwrite(self, *args, **kwargs):          # overriding save() 
    #     COD128 = barcode.get_barcode_class('code128')
    #     rv = BytesIO()
    #     name = str(30)+str(self['fund_name'])[0:2]+str(self.year_of_purchase.strftime('%Y'))+str(self.item_name)[0:2]
    #     code = COD128(name.upper(), writer=ImageWriter()).write(rv)
    #     self.barcode.save(f'{name}.png', File(rv), save=False)
    #     return super().save(*args, **kwargs)
    
    class Meta:
        model = Items
        exclude = ['barcode']
        widgets = {
            'year_of_purchase': DateInput(),
        }