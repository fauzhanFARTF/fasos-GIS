# View
from django.shortcuts import render
# Serializer
from django.core.serializers import serialize  # melakukan serialisasi menghasilkan data geojson / membuat api
# Model
from .models import MedicalFacility  # memanggil model
# Http
from django.http import HttpResponse, JsonResponse  # menghasilkan response dari api
import ast # untuk mengubah string menjadi dictionary

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