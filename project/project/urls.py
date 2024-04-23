"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fasosapp.views import home
from django.conf import settings
from django.conf.urls.static import static
from fasosapp.views import home , faskes_api, custom_api, custom_faskes_api, standart_faskes_api, medical_facility_form_add, medical_facility_list, medical_facility_form_update, medical_facility_form_delete, routing_machine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/faskes-map-api/', faskes_api, name='faskes_api'),
    path('api/custom-api/', custom_api, name='custom_api'),
    path('api/custom-faskes-api/', custom_faskes_api, name='custom_faskes_api'),
    path('api/standart-faskes-api/', standart_faskes_api, name='standart_faskes_api'),
    path('medical_facility/add/', medical_facility_form_add, name='medical_facility_form_add'),
    path('medical_facility/', medical_facility_list, name='medical_facility_list'),
    path('medical_facility/update/<int:pk>/', medical_facility_form_update, name='medical_facility_form_update'),
    path('medical_facility/delete/<int:pk>/', medical_facility_form_delete, name='medical_facility_form_delete'),
    path('routing_machine/', routing_machine , name='routing_machine'),
    
    
    # Sistem Authentication
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)