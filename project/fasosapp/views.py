# View
from django.shortcuts import render
# Serializer
from django.core.serializers import serialize  # melakukan serialisasi menghasilkan data geojson / membuat api
# Model
from .models import MedicalFacility  # memanggil model
# Http
from django.http import HttpResponse  # menghasilkan response dari api


# Create your views here.
# View
def home(request):
    return render(request, 'pages/home.html')
# API
def faskes_api(request):
    data = serialize('geojson', MedicalFacility.objects.all())
    return HttpResponse(data, content_type="json") 