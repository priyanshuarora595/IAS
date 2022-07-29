
from django import forms
from .models import Items , Funds




class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class ItemsForm(forms.ModelForm):
    
    
    class Meta:
        model = Items
        exclude = ['barcode']
        widgets = {
            'year_of_purchase': DateInput(),
        }
        
class FundsForm(forms.ModelForm):
    class Meta:
        model = Funds
        fields = '__all__'
        widgets = {
            'sanction_year': DateInput(),
        }