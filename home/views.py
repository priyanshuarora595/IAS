from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Items , Funds
from .forms import ItemsForm , FundsForm
from .resources import ItemResources
from tablib import Dataset
from IAS_Project.settings import MEDIA_ROOT
from django.db import connection as c
from pathlib import Path
import os
import pandas as pd
from io import BytesIO as IO
import xlrd
from dateutil import parser


def index(request):
    print(request.method)
    if request.user.is_authenticated:
        
        form = ItemsForm()
        context = {
            'NewEntryForm' : form
        }
        return render (request,'landing_page.html',context)
    else:
        return redirect("login")
    
def add_item(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            print(request.POST['Product_sr_no'])
            if request.POST['Product_sr_no'] not in Items.objects.values_list('Product_sr_no',flat=True):
                form = ItemsForm(request.POST)
                try:
                    form.save()
                    messages.success(request,"New item added successfully!")
                except Exception as e:
                    messages.error(request,e)
            else:
                messages.error(request,"Duplicate entry {}".format(request.POST['Product_sr_no']))
    return redirect('index')


def del_profile(request):    
        u = User.objects.get(id = request.user.id)
        if u is not None:
            u.delete()
            messages.success(request, "The user is deleted")
        else:
            messages.error(request, "The user not found")
            
        return redirect("index")
    
    
def all_entries(request):
    if request.user.is_authenticated:
        columns=list(Items._meta.get_fields())
        columns[0] = 'Select'
        entries=Items.objects.all().values()
        form = ItemsForm()
        funds_form = FundsForm()
        
        context = {
            'columns' : columns,
            'all_data' : entries,
            'NewEntryForm' : form,
            'funds_form':funds_form
        }
        return render(request,'All_Entry.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')

def del_item(request):
    if request.user.is_authenticated:
        passw=request.POST['del_pass']
        print(request.POST)
        print(passw)
        res=check_password(passw,request.user.password)
        if res:
            item_ids= request.POST.getlist("delete_item_list")
            item_ids = item_ids[0].split(",")
            try:
                for item in item_ids:
                    # print(item)
                    item_obj = Items.objects.get(id=item)
                    barcode_img_path = Path(str(MEDIA_ROOT)+str(item_obj.barcode))
                    os.remove(barcode_img_path)
                    item_obj.delete()
                messages.success(request,"Item deleted successfully!")
            except Exception as e:
                if str(e)=="Field 'id' expected a number but got ''.":
                    er = "select atleast one item to delete"
                    messages.error(request,er)
                else:
                    messages.error(request,e)
        else:
            messages.error(request,"Unauthorised!")    
        return redirect('all_entries')
    return redirect('index')


def edit_entry(request,it_id):
    print(request.method)
    if request.method=="GET":
        item_obj = Items.objects.get(id=int(it_id))
        # it=Items.objects.get(id=it_id)
        form = ItemsForm(instance=item_obj)
        # print(form)
        context = {
            'form' : form,
            'it_id' : it_id
        }
        return render(request,'EditEntry_page.html',context)
    
    
    
def edit_entry_submit(request):
    if request.method=="POST":
        passw=request.POST['edit_pass']
        res=check_password(passw,request.user.password)
        if res:
            it_id = request.POST['item_id']
            item_obj = Items.objects.get(id=int(it_id))
            updated_data = dict(request.POST)
            del updated_data['csrfmiddlewaretoken']
            del updated_data['item_id']
            for k,v in updated_data.items():
                if k=='fund_name':
                    print(v[0])
                    setattr(item_obj,k,Funds.objects.get(id=v[0]))
                elif k=="year_of_purchase":
                    print(v)
                    setattr(item_obj,k,parser.parse(v[0]))
                else:
                    setattr(item_obj,k,v[0])
                
            # print("form ========================================== \n")
            try:
                item_obj.save_overwrite()  
                messages.success(request,"Item updated successfully!")
                
            except Exception as e:
                messages.error(request,e)
        else:
            messages.error(request,"Unauthorised!")    
        
        return redirect('all_entries')
    
    
def add_funds(request):
    if request.user.is_authenticated:
        form = FundsForm(request.POST)
        try:
            form.save()
            messages.success(request,"Success")
        except Exception as e:
            messages.error(request,e)
        
    return redirect('all_entries')
        
    
    
    
    
    
def simple_upload(request):
    flag=0
    resource = ItemResources()
    if request.method =="POST":
        dataset = Dataset()
        
        try:
            new_item = request.FILES['myfile']
            
            
        except :
            e="NO file selected!"
            messages.error(request,e)
            return redirect('all_entries')
        
        extension = new_item.name.split(".")[-1].lower()
        
        if new_item.name.endswith('xlsx'):
            imported_data = dataset.load(new_item.read(),format='xlsx')
        elif new_item.name.endswith('xls'):
            imported_data = dataset.load(new_item.read(), format=extension)
        elif new_item.name.endswith('csv'):
            imported_data = dataset.load(new_item.read().decode('utf-8'), format=extension)
            
            print((imported_data))
        else:
            messages.info(request,'Wrong format !! We support only xlsx ,xls and csv files.')
            return redirect('all_entries')
        
        result = resource.import_data(imported_data, dry_run=True, collect_failed_rows=True, raise_errors=False,)
        print(result)
        if result.has_validation_errors() or result.has_errors():
                print("error", result.invalid_rows)
        
        else:
            result = resource.import_data(imported_data, dry_run=False, raise_errors=False)
        
        # for data in imported_data:
            
        #     table_cols = [f.name for f in Items._meta.get_fields()]
        #     table_cols.remove('id')
        #     table_cols.remove('barcode')
            
        #     data_dict = {k:v for k,v in zip(table_cols,data)}
            
        #     value=Items()
        #     for k,v in data_dict.items():
        #         if k=='fund_name':
        #             setattr(value,k,Funds.objects.get(fund_name=v))
        #         elif k=="year_of_purchase":
        #             setattr(value,k,parser.parse(v))
        #         else:
        #             setattr(value,k,v)
        
            # try:
            #     if data_dict['Product_sr_no'] not in Items.objects.values_list('Product_sr_no',flat=True):
            #         value.save()
            #     else:
            #         if flag==0:
            #             messages.error(request,"Duplicate entry {}".format(data_dict['Product_sr_no']))
            #             flag=1
            # except Exception as e:
            #     if flag==0:
            #         messages.error(request,e)
            #         flag=1
            #     continue
        if flag==0:
            messages.success(request,"data import successful")
    return redirect('all_entries')




def add_media_path(x):
    x=str(x)
    x=str(MEDIA_ROOT)+"\\"+x
    x=Path(x)
    return x
    
            
def export_xlsx(request):
    dataset = ItemResources().export()
    df_output = dataset.export('df')
    print(df_output)
    df_output = df_output.drop(columns=['id'],axis=1)
    df_output['barcode'] = df_output['barcode'].apply(add_media_path)
    excel_file = IO()
    xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')

    df_output.to_excel(xlwriter, 'sheetname',index=False)
    xlwriter.save()
    xlwriter.close()
    
    excel_file.seek(0)
    
    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # set the file name in the Content-Disposition header
    response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'

    return response



def export_csv(request):
    dataset = ItemResources().export()
    df_output = dataset.export('df')
    df_output = df_output.drop(columns=['id'],axis=1)
    df_output['barcode'] = df_output['barcode'].apply(add_media_path)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename.csv'

    df_output.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    return response

def scan_barcode(request):
    if request.user.is_authenticated:
        columns=Items._meta.get_fields()
        form = ItemsForm()
        code = request.POST['mybarcode']
        code = "barcodes/"+str(code)+".png"
        # print(code)
        entries=Items.objects.filter(barcode = code).values()
        # all_entries = Items.objects.all().values()
        # print('filtered entries = ',entries)
        # print('all entries = ',all_entries)
        context = {
            'columns' : columns,
            'all_data' : entries,
            'NewEntryForm' : form,
        }
        return render(request,'All_Entry.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')


