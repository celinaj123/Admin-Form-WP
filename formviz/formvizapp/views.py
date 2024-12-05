from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MapRowSec

def form(request):
    rows = MapRowSec.objects.all()
    return render(request, 'form.html', {'rows': rows})


def add_map_rowsec(request):
    if request.method == 'POST':
        usr_access = request.POST.get('usr_access')
        param = request.POST.get('param')
        paramvalue = request.POST.get('paramvalue')
        dashboard_id = request.POST.get('dashboard_id')

        if usr_access and param and paramvalue and dashboard_id:
            new_record = MapRowSec(
                usr_access=usr_access,
                param=param,
                paramvalue=paramvalue,
                dashboard_id=dashboard_id
            )
            new_record.save()
            return redirect('form')  
        else:
            return HttpResponse("<script>alert('All fields are required!'); window.history.back();</script>")
    
    return render(request, 'form.html') 

def delete_map_rowsec(request, record_id):
    record = get_object_or_404(MapRowSec, id=record_id)
    
    if request.method == 'POST':
        record.delete()  
        return redirect('form') 
    return render(request, 'form.html', {'record': record})

def update_map_rowsec(request, record_id):
    record = get_object_or_404(MapRowSec, id=record_id)
    
    if request.method == 'POST':
        record.usr_access = request.POST.get('usr_access')
        record.param = request.POST.get('param')
        record.paramvalue = request.POST.get('paramvalue')
        record.dashboard_id = request.POST.get('dashboard_id')
        record.save()
        return redirect('form')
    return render(request, 'form.html', {'form': form,'record': record})