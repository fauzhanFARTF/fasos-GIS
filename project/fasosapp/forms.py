from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import MedicalFacility

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
