# View
from django.shortcuts import render, redirect, get_object_or_404
# Serializer
from django.core.serializers import serialize  # melakukan serialisasi menghasilkan data geojson / membuat api
# Model
from .models import MedicalFacility  # memanggil model
# Medical Facility Form
from .forms import MedicalFacilityForm
# Http
from django.http import HttpResponse, JsonResponse  # menghasilkan response dari api
import ast # untuk mengubah string menjadi dictionary
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
            return redirect('medical_facility_list')
    context = {
        'form' : form
    }
    return render(request,'pages/medical_facility_update.html', context)
