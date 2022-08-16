from django.core.cache import cache
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, JsonResponse
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
import json
from dateutil import parser


def index(request):
    # print(request.method)
    if request.user.is_authenticated:
        funds=Funds.objects.all()
        form = ItemsForm()
        context = {
            'NewEntryForm' : form,
            'funds' : funds
        }
        return render (request,'landing_page.html',context)
    else:
        return redirect("login")
    
def add_item(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # print(request.POST['Product_sr_no'])
            if request.POST['Product_sr_no'] not in Items.objects.values_list('Product_sr_no',flat=True):
                form = ItemsForm(request.POST)
                try:
                    form.save()
                    messages.success(request,"New item added successfully!")
                except Exception as e:
                    messages.error(request,e)
            else:
                messages.error(request,"Duplicate entry {}".format(request.POST['Product_sr_no']))
    return redirect('all_entries')


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
        funds=Funds.objects.all()
        # entries=Items.objects.filter(fund_name='F1').values()
        # print(entries)
        form = ItemsForm()
        funds_form = FundsForm()
        # print(entries)
        
        context = {
            'columns' : columns,
            'all_data' : entries,
            'NewEntryForm' : form,
            'funds_form':funds_form,
            'funds' : funds
        }
        return render(request,'All_Entry.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')

def all_funds(request):
    if request.user.is_authenticated:
        columns=list(Funds._meta.get_fields())
        # columns[0] = 'Select'
        entries=Funds.objects.all().values()
        funds=Funds.objects.all()
        funds_form = FundsForm()
        del columns[0]
        context = {
            'columns' : columns,
            'all_data' : entries,
            'funds_form':funds_form,
            'funds' : funds
        }
        return render(request,'Funds.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')



def filter_data(request):
    # print(request.POST)
    columns=list(Items._meta.get_fields())
    form = ItemsForm()
    funds_form = FundsForm()
    funds=Funds.objects.all()
    try:
        filter_by=request.POST['filter_by']
        if filter_by=='Fund':
            fund_name_inp=request.POST['Fund']
            entries=Items.objects.filter(fund_name=fund_name_inp).values()
            # request.session['last_query']=pd.DataFrame.from_records(entries).to_dict()
            # cache.set('last_query',entries)
            request.session['last_query'] = {'filter_by':'fund_name','val':fund_name_inp}
        elif filter_by=='Year':
            # print("year====================================================")
            year_inp = request.POST['year']
            entries=Items.objects.filter(year_of_purchase__year=year_inp).values()
            request.session['last_query'] = {'filter_by':'year_of_purchase__year','val':year_inp}
        
        elif filter_by=="FNY":
            fund_name_inp=request.POST['Fund']
            year_inp = request.POST['year']
            entries=Items.objects.filter(fund_name=fund_name_inp,year_of_purchase__year=year_inp).values()
            request.session['last_query'] = {'filter_by1':'fund_name','val1':fund_name_inp,'filter_by2':'year_of_purchase__year','val2':year_inp}
            
        else:
            entries=Items.objects.all().values()
            
    except:
        return redirect('all_entries')
    context = {
            'columns' : columns,
            'all_data' : entries,
            'NewEntryForm' : form,
            'funds_form':funds_form,
            'funds' : funds
        }
    return render(request,'All_Entry.html',context)




def del_item(request):
    if request.user.is_authenticated:
        passw=request.POST['del_pass']
        # print(request.POST)
        # print(passw)
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



def del_fund(request):
    if request.user.is_authenticated:
        passw=request.POST['del_pass']
        # print(request.POST)
        # print(passw)
        res=check_password(passw,request.user.password)
        if res:
            item_ids= request.POST.getlist("delete_funds_list")
            item_ids = item_ids[0].split(",")
            try:
                for item in item_ids:
                    # print(item)
                    item_obj = Funds.objects.get(fund_name=item)
                    # barcode_img_path = Path(str(MEDIA_ROOT)+str(item_obj.barcode))
                    # os.remove(barcode_img_path)
                    item_obj.delete()
                messages.success(request,"Fund deleted successfully!")
            except Exception as e:
                if str(e)=="Field 'id' expected a number but got ''.":
                    er = "select atleast one item to delete"
                    messages.error(request,er)
                else:
                    messages.error(request,e)
        else:
            messages.error(request,"Unauthorised!")    
        return redirect('all_funds')
    return redirect('index')


def edit_entry(request,it_id):
    # print(request.method)
    if request.method=="GET":
        try:
            item_obj = Items.objects.get(id=int(it_id))
            # it=Items.objects.get(id=it_id)
            form = ItemsForm(instance=item_obj)
            # print(form)
            context = {
                'form' : form,
                'it_id' : it_id
            }
        except Exception as e:
            messages.error(request,'At least select any item')
        return render(request,'EditEntry_page.html',context)
    
    
    
def edit_entry_submit(request):
    if request.method=="POST":
        passw=request.POST['edit_pass']
        res=check_password(passw,request.user.password)
        if res:
            it_id = request.POST['item_id']
            try:    
                item_obj = Items.objects.get(id=int(it_id))
                updated_data = dict(request.POST)
                del updated_data['csrfmiddlewaretoken']
                del updated_data['item_id']
                for k,v in updated_data.items():
                    if k=='fund_name':
                        setattr(item_obj,k,Funds.objects.get(fund_name=v[0]))
                    elif k=="year_of_purchase":
                        # print(v)
                        setattr(item_obj,k,parser.parse(v[0]))
                    else:
                        setattr(item_obj,k,v[0])
            except Exception as e:
                messages.error(request,'At least select any item')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            try:
                item_obj.save_overwrite()  
                messages.success(request,"Item updated successfully!")
                
            except Exception as e:
                messages.error(request,e)
        else:
            messages.error(request,"Unauthorised!")    
        
        return redirect('all_entries')
    

def edit_fund(request,it_id):
    # print(request.method)
    if request.method=="GET":
        try:
            if "%20" in it_id:
                it_id.replace("%20"," ")
            item_obj = Funds.objects.get(fund_name=it_id)
            # it=Items.objects.get(id=it_id)
            form = FundsForm(instance=item_obj)
            
            # print(form)
            context = {
                'form' : form,
                'it_id' : it_id
            }
        except Exception as e:
            messages.error(request,'At least select any item')
        return render(request,'EditEntry_page.html',context)    
    
    
    
def edit_fund_submit(request):
    if request.method=="POST":
        passw=request.POST['edit_pass']
        res=check_password(passw,request.user.password)
        if res:
            it_id = request.POST['item_id']
            try:    
                item_obj = Funds.objects.get(fund_name=it_id)
                updated_data = dict(request.POST)
                del updated_data['csrfmiddlewaretoken']
                del updated_data['item_id']
                
                for k,v in updated_data.items():
                    print(k)
                    if k=='fund_name':
                        pass
                    elif k=="sanction_year":
                        # print(v)
                        setattr(item_obj,k,parser.parse(v[0]))
                    else:
                        setattr(item_obj,k,v[0])
            except Exception as e:
                messages.error(request,e)
                print(e)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            try:
                item_obj.save()  
                messages.success(request,"Item updated successfully!")
                
            except Exception as e:
                print(e)
                messages.error(request,e)
        else:
            messages.error(request,"Unauthorised!")    
        
        return redirect('all_funds')
    


def add_funds(request):
    if request.user.is_authenticated:
        form = FundsForm(request.POST)
        try:
            form.save()
            messages.success(request,"Success")
        except Exception as e:
            messages.error(request,e)
        
    return redirect('all_entries')
        
    
    
def fund_date(request,it_id):
    if "%20" in it_id:
        it_id=it_id.replace("%20"," ")
    item_obj = Funds.objects.get(fund_name=it_id)
    # print(item_obj.sanction_year)
    # print("===============================")
    return JsonResponse({"min_date":str(item_obj.sanction_year).split('-')})
    
    
def simple_upload(request):
    flag=0
    # resource = ItemResources()
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
            imported_data = pd.read_csv(new_item)
            GFG = pd.ExcelWriter('test.xlsx')
            imported_data.to_excel(GFG,index=False)
            
            # print(imported_data)
            
            
            
    
        else:
            messages.info(request,'Wrong format !! We support only xlsx ,xls and csv files.')
            return redirect('all_entries')
        
        # result = resource.import_data(imported_data, dry_run=True, collect_failed_rows=True, raise_errors=False,)
        # print(result)
        # if result.has_validation_errors() or result.has_errors():
        #         print("error", result.invalid_rows)
        
        # else:
        #     result = resource.import_data(imported_data, dry_run=False, raise_errors=False)
        
        for data in imported_data:
            table_cols = [f.name for f in Items._meta.get_fields()]
            table_cols.remove('id')
            table_cols.remove('barcode')
            
            data_dict = {k:v for k,v in zip(table_cols,data)}
            
            value=Items()
            for k,v in data_dict.items():
                if k=='fund_name':
                    setattr(value,k,Funds.objects.get(fund_name=v))
                elif k=="year_of_purchase":
                    print(v)
                    setattr(value,k,parser.parse(v))
                else:
                    setattr(value,k,v)
        
            try:
                if data_dict['Product_sr_no'] not in Items.objects.values_list('Product_sr_no',flat=True):
                    value.save()
                else:
                    if flag==0:
                        messages.error(request,"Duplicate entry {}".format(data_dict['Product_sr_no']))
                        flag=1
            except Exception as e:
                if flag==0:
                    messages.error(request,e)
                    flag=1
                continue
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
    
    try:
        if request.session['last_query']:
            x=request.session['last_query']
            if len(x)>2:
                filter_by1 = x['filter_by1']
                filter_val1 = x['val1']
                filter_by2 = x['filter_by2']
                filter_val2 = x['val2']
                kwargs = {
                    '{0}'.format(filter_by1): filter_val1,
                    '{0}'.format(filter_by2): filter_val2,
                }
            else:
                
                filter_by = x['filter_by']
                filter_val = x['val']
                
                kwargs = {
                    '{0}'.format(filter_by): filter_val,
                }
            query=Items.objects.filter(**kwargs)
            # print(query)
            dataset = ItemResources().export(queryset=query)
    except Exception as e:
         messages.error(request,e)
    df_output = dataset.export('df')
    # print(df_output)
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


def export_xls(request):
    dataset = ItemResources().export()
    try:
        if request.session['last_query']:
            x=request.session['last_query']
            if len(x)>2:
                filter_by1 = x['filter_by1']
                filter_val1 = x['val1']
                filter_by2 = x['filter_by2']
                filter_val2 = x['val2']
                kwargs = {
                    '{0}'.format(filter_by1): filter_val1,
                    '{0}'.format(filter_by2): filter_val2,
                }
            else:
                
                filter_by = x['filter_by']
                filter_val = x['val']
                
                kwargs = {
                    '{0}'.format(filter_by): filter_val,
                }
            query=Items.objects.filter(**kwargs)
            # print(query)
            dataset = ItemResources().export(queryset=query)
    except Exception as e:
        messages.error(request,e)
    df_output = dataset.export('df')
    # print(df_output)
    df_output = df_output.drop(columns=['id'],axis=1)
    df_output['barcode'] = df_output['barcode'].apply(add_media_path)
    excel_file = IO()
    xlwriter = pd.ExcelWriter(excel_file, engine='xlwt')

    df_output.to_excel(xlwriter, 'sheetname',index=False)
    xlwriter.save()
    xlwriter.close()
    
    excel_file.seek(0)
    
    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # set the file name in the Content-Disposition header
    response['Content-Disposition'] = 'attachment; filename=myfile.xls'

    return response


def export_csv(request):
    dataset = ItemResources().export()
    try:
        if request.session['last_query']:
            x=request.session['last_query']
            if len(x)>2:
                filter_by1 = x['filter_by1']
                filter_val1 = x['val1']
                filter_by2 = x['filter_by2']
                filter_val2 = x['val2']
                kwargs = {
                    '{0}'.format(filter_by1): filter_val1,
                    '{0}'.format(filter_by2): filter_val2,
                }
            else:
                
                filter_by = x['filter_by']
                filter_val = x['val']
                
                kwargs = {
                    '{0}'.format(filter_by): filter_val,
                }
            query=Items.objects.filter(**kwargs)
            # print(query)
            dataset = ItemResources().export(queryset=query)
    except Exception as e:
        messages.error(request,e)
    df_output = dataset.export('df')
    # print(df_output)
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
        if len(entries)==0:
            messages.error(request,"No Entry found!")
        return render(request,'All_Entry.html',context)
    else:
        messages.error(request,"UNAUTHENTICATED!")
    return redirect('index')


