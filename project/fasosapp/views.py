# View
from django.shortcuts import render, redirect, get_object_or_404
# Serializer
from django.core.serializers import serialize  # melakukan serialisasi menghasilkan data geojson / membuat api
# Model
from .models import MedicalFacility, LocalGovernmentOffice, CCTVETLE, BatasKecamatan  # memanggil model
# Facility Form
from .forms import MedicalFacilityForm, LocalGovernmentOfficeForm, CCTVETLEForm, CCTVETLEFormRead, MedicalFacilityFormRead, LocalGovernmentOfficeFormRead
# Http
from django.http import HttpResponse, JsonResponse  # menghasilkan response dari api
import ast # untuk mengubah string menjadi dictionary
from django.contrib import messages

# Form MedicalFacility

# Create your views here.
# View
def home(request):
    return render(request, 'pages/home.html')

# API
def faskes_api(request):
    data = serialize('geojson', MedicalFacility.objects.all())
    return HttpResponse(data, content_type="json") 

# Custom API
def custom_api(request):
    data = {
        'nama' : 'Fauzan',
        'usia' : '33 Tahun',
        'perempuan' : 'False'
    }
    return JsonResponse(data)

# Custom Map API
def custom_faskes_api(request):
    # Mengambil data dari model
    features = {
        'type': 'FeatureCollection',
        'crs' : {
            'type': 'name',
            'properties': {
                'name' : 'EPSG:4326'
            },
        },
        'features' : []
    }
    model = MedicalFacility.objects.all()
    # Mengambil data dari model
    for item in model:
        # print(item)
        # print(item.nama)
        feature = {
            "type" :"Feature",
            "properties" : 
                {
                    'nama' : item.nama,
                    'jenis' : item.jenis,
                    'tingkatan' : item. tingkatan,
                    'status' : item.status
                },
            "geometry": ast.literal_eval(item.location.json),
        }
        features['features'].append(feature) # Menambahkan feature ke dalam features
    print(features)
    return JsonResponse(features, safe=False)

# Standart Map API
def standart_faskes_api(request):
    data = serialize('geojson', MedicalFacility.objects.all())
    return HttpResponse(data, content_type="application/json") 

# Medical Facility Form Add
def medical_facility_form_add(request):
    # pass
    if request.method == 'POST':
        form = MedicalFacilityForm(request.POST, request.FILES)
        if form.is_valid():
            # logic for post data
            # return 'Hello World'
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Tambah Data Berhasil")
            return redirect('home')

    else :
        form = MedicalFacilityForm()
        
    context =  {
       'form' : form 
    }
    return render(request,'pages/medical_facility_add.html', context)

# Medical Facility List
def medical_facility_list(request):
    context = {
        # 'data' : MedicalFacility.objects.all()
        'data' : MedicalFacility.objects.filter(operator = request.user)

    }
    return render(request,'pages/medical_facility_list.html', context)

# Medical Facility Update
def medical_facility_form_update(request , pk):
    objek = get_object_or_404(MedicalFacility, id=pk)
    form = MedicalFacilityForm(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Ubah Data Berhasil")
            return redirect('medical_facility_list')
    context = {
        'form' : form
    }
    return render(request,'pages/medical_facility_update.html', context)

# Medical Facility Delete
def medical_facility_form_delete(request, pk):
    objek = get_object_or_404(MedicalFacility, id=pk)
    form = MedicalFacilityFormRead(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        objek.delete()
        messages.success(request,"Hapus Data Berhasil")
        return redirect('medical_facility_list')
    context = {
        'form' : form
    }
    return render(request, 'pages/medical_facility_delete.html', context)

# Routing Machine
def routing_machine(request):
    return render(request, 'pages/routing_machine.html')

def standart_opd_api(request):
    data = serialize('geojson',LocalGovernmentOffice.objects.all())
    return HttpResponse(data, content_type="application/json") 

def local_government_office_form_add(request):
    # pass
    if request.method == 'POST':
        form = LocalGovernmentOfficeForm(request.POST, request.FILES)
        if form.is_valid():
            # logic for post data
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Tambah Data Berhasil")
            return redirect('home')

    else :
        form = LocalGovernmentOfficeForm()
        
    context =  {
       'form' : form 
    }
    return render(request,'pages/local_government_office_add.html', context)

def local_government_office_list(request):
    context = {
        # 'data' : MedicalFacility.objects.all()
        'data' : LocalGovernmentOffice.objects.filter(operator = request.user)
    }
    return render(request,'pages/local_government_office_list.html', context)

def local_government_office_form_update(request , pk):
    objek = get_object_or_404(LocalGovernmentOffice, id=pk)
    form = LocalGovernmentOfficeForm(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Ubah Data Berhasil")
            return redirect('local_government_office_list')
    context = {
        'form' : form
    }
    return render(request,'pages/local_government_office_update.html', context)

def local_government_office_form_delete(request, pk):
    objek = get_object_or_404(LocalGovernmentOffice, id=pk)
    form = LocalGovernmentOfficeFormRead(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        objek.delete()
        messages.success(request,"Hapus Data Berhasil")
        return redirect('local_government_office_list')
    context = {
        'form' : form
    }
    return render(request, 'pages/local_government_office_delete.html', context)

def standart_cctv_etle_api(request):
    data = serialize('geojson',CCTVETLE.objects.all())
    return HttpResponse(data, content_type="application/json")

def cctv_etle_list(request):
    context = {
        # 'data' : MedicalFacility.objects.all()
        'data' : CCTVETLE.objects.filter(operator = request.user)
    }
    return render(request,'pages/cctv_etle_list.html', context)

def cctv_etle_form_add(request):
    # pass
    if request.method == 'POST':
        form = CCTVETLEForm(request.POST, request.FILES)
        if form.is_valid():
            # logic for post data
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Tambah Data Berhasil")
            return redirect('home')

    else :
        form = CCTVETLEForm()
        
    context =  {
       'form' : form 
    }
    return render(request,'pages/cctv_etle_add.html', context)

def cctv_etle_form_update(request , pk):
    objek = get_object_or_404(CCTVETLE, id=pk)
    form = CCTVETLEForm(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.operator = request.user
            data.save()
            messages.success(request,"Ubah Data Berhasil")
            return redirect('cctv_etle_list')
    context = {
        'form' : form
    }
    return render(request,'pages/cctv_etle_update.html', context)

def cctv_etle_form_delete(request, pk):
    objek = get_object_or_404(CCTVETLE, id=pk)
    form = CCTVETLEFormRead(request.POST or None, request.FILES or None, instance=objek)
    
    if request.method == 'POST':
        objek.delete()
        messages.success(request,"Hapus Data Berhasil")
        return redirect('cctv_etle_list')
    context = {
        'form' : form
    }
    return render(request, 'pages/cctv_etle_delete.html', context)

def batas_kecamatan_api(request):
    data = serialize('geojson',BatasKecamatan.objects.all())
    return HttpResponse(data, content_type="application/json") 
