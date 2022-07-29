from email.policy import default
from django.db import models
from djmoney.models.fields import MoneyField

from django.forms import CharField, DecimalField
from barcode import EAN13
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File 
from IAS_Project.settings import STATIC_URL



# Create your models here.
class Funds(models.Model):
    fund_name = models.CharField(verbose_name="Fund name",max_length=30,blank=False,unique=True)
    sanction_year = models.DateField(verbose_name="Year",blank=False)
    balance = models.FloatField(verbose_name="Balance", default=0)
    
    def __str__(self):
        return str(self.fund_name)



class Items(models.Model):
    Product_sr_no = models.CharField(verbose_name="Product Serial Number",max_length=30,blank=False,unique=True)
    item_name = models.CharField(verbose_name="Item Name",max_length=200,blank=False)
    year_of_purchase = models.DateField(verbose_name="Purchase Year",blank=False)
    # fund_name = models.CharField(verbose_name="Fund Name",max_length=200,blank=False)
    fund_name = models.ForeignKey(to='Funds', on_delete=models.DO_NOTHING)
    LP_NO = models.CharField(verbose_name="LP Number",max_length=5,blank=False)
    initial_price = models.FloatField(verbose_name="Initial Price", default=0)
    issued_to = models.CharField(verbose_name="Issued To",max_length=100)
    Depreciated_Price = models.FloatField(verbose_name="Depreciated Price",default=0)
    Remarks = models.TextField(verbose_name="Remarks",blank=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True,default="0")
    
    
    def __str__(self):
        return str(self.item_name)
    
    
    def save_overwrite(self, *args, **kwargs):          # overriding save() 
        print("original_save_function")
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):          # overriding save() 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        name = str(30)+str(self.fund_name)[0:2]+str(self.year_of_purchase.strftime('%Y'))+str(self.item_name)[0:2]
        code = COD128(name.upper(), writer=ImageWriter()).write(rv)
        self.barcode.save(f'{name.upper()}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
        
    