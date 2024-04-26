from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import MedicalFacility, LocalGovernmentOffice

LEAFLET_WIDGET_ATTRS = {
    'map_height': '500px',
    'map_width': '100%',
    'map_srid': 4326,
    'auto-include': True
}

class MedicalFacilityForm(forms.ModelForm):
    class Meta:
        model = MedicalFacility
        fields = [
            'koderumahsakit',
            'nama',
            'tipe',
            'jenis',
            'tingkatan',
            'kepemilikan',
            'alamat',
            'no_telp',
            'status',
            'hari_beroperasi',
            'jam_beroperasi',
            'location',
            'photo'
            ]
        widgets = {'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}
        
        
class LocalGovernmentOfficeForm(forms.ModelForm):
    class Meta:
        model = LocalGovernmentOffice
        fields = [
            'nama',
            'tipe',
            'alamat',
            'no_telp',
            'status',
            'hari_beroperasi',
            'jam_beroperasi',
            'location',
            'photo'
            ]
        widgets = {'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}

