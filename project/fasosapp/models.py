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
    
    SPESIFIC_CHOICES =[
        ('Rumah Sakit Umum','Rumah Sakit Umum'),
        ('Rumah Sakit Khusus','Rumah Sakit Khusus'),
        ('-', '-')
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
        ('Kelas A', 'Kelas A'),
        ('Kelas B', 'Kelas B'),
        ('Kelas C', 'Kelas C'),
        ('Belum Mengisi Tingkatan', 'Belum Mengisi Tingkatan'),
        ('-', '-')
    ]
    
    DAYS_CHOICES = [
        ('Setiap Hari', 'Setiap Hari'),
        ('Senin - Jumat', 'Senin - Jumat'),
        ('Sabtu - Minggu', 'Sabtu - Minggu')
    ]
    
    OWNERSHIP_STATUS_CHOICES = [
        ('Dikelola Pemerintah', 'Dikelola Pemerintah'),
        ('Dikelola Swasta', 'Dikelola Swasta'),
        ('Dikelola Organisasi Sosial', 'Dikelola Organisasi Sosial'),
        ('Belum Mengisi Penyelenggara', 'Belum Mengisi Penyelenggara'),
        ('-', '-')
    ]
    
    koderumahsakit = models.CharField(max_length=10)
    nama = models.CharField(max_length=150)
    tipe = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Rumah Sakit')
    jenis = models.CharField(max_length=50, choices=SPESIFIC_CHOICES, default='Rumah Sakit Umum')
    tingkatan = models.CharField(max_length=50, choices=LEVEL_CHOICES, default='Belum Mengisi Tingkatan')
    kepemilikan = models.CharField(max_length=50, choices=OWNERSHIP_STATUS_CHOICES, default='Belum Mengisi Penyelenggara')
    alamat = models.TextField(max_length=255)
    no_telp = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Perencanaan/Pengajuan')
    # beroperasi = models.BooleanField(default=False)
    hari_beroperasi = models.CharField(max_length=50, choices=DAYS_CHOICES, default='Setiap Hari')
    jam_beroperasi = models.CharField(max_length=50)
    location = models.PointField(srid=4326, spatial_index=True)
    photo = models.ImageField(upload_to='medical_facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_field = models.DateTimeField(auto_now=True)


class LocalGovernmentOffice(models.Model) :
    STATUS_CHOICES = [
        ('Perencanaan/Pengajuan', 'Perencanaan/Pengajuan'),
        ('Dalam Masa Peninjauan', 'Dalam Masa Peninjauan'),
        ('Perencanaan Dibatalkan', 'Perencanaan Dibatalkan'),
        ('Dalam Masa Pembangunan', 'Dalam Masa Pembangunan'),
        ('Pembangunan Selesai/Belum Beroperasi', 'Pembangunan Selesai/Belum Beroperasi'),
        ('Pembangunan Selesai/Sudah Beroperasi', 'Pembangunan Selesai/Sudah Beroperasi'),
        ('Tutup/Sudah Tidak Beroperasi', 'Tutup/Sudah Tidak Beroperasi')
    ]
    DAYS_CHOICES = [
        ('Setiap Hari', 'Setiap Hari'),
        ('Senin - Jumat', 'Senin - Jumat'),
        ('Sabtu - Minggu', 'Sabtu - Minggu')
    ]
    SPESIFIC_CHOICES =[
        ('Perangkat Daerah','Perangkat Daerah'),
        ('Instansi Vertikal','Instansi Vertikal'),
    ]
    
    nama = models.CharField(max_length=150)
    tipe = models.CharField(max_length=50, choices=SPESIFIC_CHOICES, default='Perangkat Daerah')
    alamat = models.TextField(max_length=255)
    no_telp = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Perencanaan/Pengajuan')
    hari_beroperasi = models.CharField(max_length=50, choices=DAYS_CHOICES)
    jam_beroperasi = models.CharField(max_length=50)
    location = models.PointField(srid=4326, spatial_index=True)
    photo = models.ImageField(upload_to='local_government_office')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_field = models.DateTimeField(auto_now=True)