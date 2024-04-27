from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import MedicalFacility, LocalGovernmentOffice, CCTVETLE
from datetime import date

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
   
today = date.today()
 
class CCTVETLEForm(forms.ModelForm):
    # target_Date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date'}), required=True)
    # tgl_pemasangan = forms.DateField(widget=forms.TextInput(attrs={'value': today, 'type': 'date'}), required=True)

    class Meta:
        model = CCTVETLE
        fields = [
            'kode_cam',
            'nama_lokasi',
            'wilayah',
            'sn_camera',
            'sn_modem',
            'tgl_pemasangan',
            'is_active',
            'location',
            'photo'
            ]
        widgets = {'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}