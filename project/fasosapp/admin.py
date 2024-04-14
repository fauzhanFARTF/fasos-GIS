# from django.contrib import admin      # Admin Non Spatial
from django.contrib.gis  import admin   # Admin Spatial
from .models import MedicalFacility

# Register your models here.
class LocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 10
    default_lon = 11859737.83338
    default_lat = -696023.89962

@admin.register(MedicalFacility)
class MedicalFacilityAdmin(LocationAdmin):
    list_filter = ['status', 'operator'] 
    list_display = ['id', 'nama','jenis','tingkatan','status', 'operator']

# admin.site.register(MedicalFacility)
# class MedicalFacilityAdmin(LocationAdmin):
#     list_filter = ['status', 'operator']
#     list_display = ['id', 'nama','jenis','tingkatan','status', 'operator']