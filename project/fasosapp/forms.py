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
LEAFLET_WIDGET_ATTRS_READ = {
    'map_height': '500px',
    'map_width': '100%',
    'map_srid': 4326,
    'auto-include': True,
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
        
class MedicalFacilityFormRead(forms.ModelForm):
    koderumahsakit = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    nama = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    jenis = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = MedicalFacility
        exclude = [
            'tipe',
            'tingkatan',
            'kepemilikan',
            'is_active',
            'no_telp',
            'status',
            'hari_beroperasi',
            'jam_beroperasi',
            'photo'
        ]
        fields = [
            'koderumahsakit',
            'nama',
            'jenis',
            'alamat',
            'location'
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

class LocalGovernmentOfficeFormRead(forms.ModelForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    tipe = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = LocalGovernmentOffice
        exclude = [           
            'no_telp',
            'status',
            'hari_beroperasi',
            'jam_beroperasi',
            'photo'         
        ]
        fields = [
            'nama',
            'tipe',
            'alamat',
            'location'
            ]
        widgets = {'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}
   
today = date.today()
 
class CCTVETLEForm(forms.ModelForm):
    # target_Date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date'}), required=True)
    tgl_pemasangan = forms.DateField(widget=forms.TextInput(attrs={'value': today, 'type': 'date'}), required=True)

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

class CCTVETLEFormRead(forms.ModelForm):
    # target_Date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date'}), required=True)
    # tgl_pemasangan = forms.DateField(widget=forms.TextInput(attrs={'value': today, 'type': 'date'}), required=True)
    kode_cam = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    nama_lokasi = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    wilayah = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = CCTVETLE
        exclude = [
            'sn_camera',
            'sn_modem',
            'tgl_pemasangan',
            'is_active',   
        ]
        fields = [
            'kode_cam',
            'nama_lokasi',
            'wilayah',
            'location',
            ]
        widgets = {
            'location': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS_READ)
        }