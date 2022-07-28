
from asyncio.windows_events import NULL
from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Items 
from .forms import ItemsForm
from .resources import ItemResources
from tablib import Dataset
from IAS_Project.settings import MEDIA_ROOT
from django.db import connection as c
from pathlib import Path
import os
import pandas as pd
from io import BytesIO as IO


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
            form = ItemsForm(request.POST)
            # print(form)
            try:
                # print(request.POST)
                # Items.save_overwrite(request.POST)
                form.save()
                messages.success(request,"New item added successfully!")
            except Exception as e:
                print(e)
                messages.error(request,"Error occurred. Data Entry Failed!")
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
        columns=Items._meta.get_fields()
        entries=Items.objects.all().values()
        form = ItemsForm()
        
        context = {
            'columns' : columns,
            'all_data' : entries,
            'NewEntryForm' : form,
        }
        return render(request,'All_Entry.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')

def del_item(request):
    if request.user.is_authenticated:
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
        it_id = request.POST['item_id']
        print(it_id);
        item_obj = Items.objects.get(id=int(it_id))
        updated_data = dict(request.POST)
        del updated_data['csrfmiddlewaretoken']
        del updated_data['item_id']
        for k,v in updated_data.items():
            setattr(item_obj,k,v[0])
        # print("form ========================================== \n")
        try:
            item_obj.save_overwrite()  
            messages.success(request,"Item updated successfully!")
            
        except Exception as e:
            messages.error(request,e)
        
        return redirect('all_entries')
    
    
def simple_upload(request):
    if request.method =="POST":
        item_resource = ItemResources()
        dataset = Dataset()
        new_item = request.FILES['myfile']
        
        if not new_item.name.endswith('xlsx'):
            messages.info(request,'Wrong format !! We support only xlsx files.')
            return redirect('all_entries')
        
        imported_data = dataset.load(new_item.read(),format='xlsx')
        for data in imported_data:
            table_cols = [f.name for f in Items._meta.get_fields()]
            table_cols.remove('id')
            table_cols.remove('barcode')
            data_dict = {k:v for k,v in zip(table_cols,data)}
            value = Items(**data_dict)
            value.save()
        
        messages.success(request,"data import successful")
    return redirect('all_entries')

            
            
def export(request):
    dataset = ItemResources().export()
    # print(type(dataset))
    df_output = dataset.export('df')
    # print(type(df_output))
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


def get_data_from_barcode(request):
    pass