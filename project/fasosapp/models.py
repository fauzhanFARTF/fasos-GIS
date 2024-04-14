# from django.db import models # Model Database NonSpasial
from django.contrib.gis.db import models # Model Database Spasial
from django.contrib.auth.models import User

# Create your models here.
class MedicalFacility(models.Model) :
    TYPE_CHOICES =[
        ('Rumah Sakit','Rumah Sakit'),
        ('Puskesmas','Puskesmas'),
        ('Klinik', 'Klinik'),
        ('Apotik', 'Apotik')
    ]
    
    STATUS_CHOICES = [
        ('Perencanaan/Pengajuan', 'Perencanaan/Pengajuan'),
        ('Dalam Masa Peninjauan', 'Dalam Masa Peninjauan'),
        ('Perencanaan Dibatalkan', 'Perencanaan Dibatalkan'),
        ('Dalam Masa Pembangunan', 'Dalam Masa Pembangunan'),
        ('Pembangunan Selesai/Belum Beroperasi', 'Pembangunan Selesai/Belum Beroperasi'),
        ('Pembangunan Selesai/Sudah Beroperasi', 'Pembangunan Selesai/Sudah Beroperasi'),
        ('Tutup/Sudah Tidak Beroperasi', 'Tutup/Sudah Tidak Beroperasi')
    ]
    
    LEVEL_CHOICES = [
        ('Fasilitas Kesehatan Tingkat 1', 'Fasilitas Kesehatan Tingkat 1'),
        ('Fasilitas Kesehatan Tingkat 2', 'Fasilitas Kesehatan Tingkat 2'),
        ('Fasilitas Kesehatan Tingkat 3', 'Fasilitas Kesehatan Tingkat 3')
    ]
    
    DAYS_CHOICES = [
        ('Setiap Hari', 'Setiap Hari'),
        ('Senin - Jumat', 'Senin - Jumat'),
        ('Sabtu - Minggu', 'Sabtu - Minggu')
    ]
    
    nama = models.CharField(max_length=50)
    jenis = models.CharField(max_length=30, choices=TYPE_CHOICES, default='Rumah Sakit')
    tingkatan = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    alamat = models.TextField(max_length=255)
    no_telp = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Perencanaan/Pengajuan')
    # beroperasi = models.BooleanField(default=False)
    hari_beroperasi = models.CharField(max_length=50, choices=DAYS_CHOICES)
    jam_beroperasi = models.CharField(max_length=50)
    location = models.PointField(srid=4326, spatial_index=True)
    photo = models.ImageField(upload_to='medical_facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_field = models.DateTimeField(auto_now=True)