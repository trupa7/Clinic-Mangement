"""medicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('records/', include('records.urls', namespace='records')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('nurses/', include('nurses.urls', namespace='nurses')),
    path('lab/', include('laboratory.urls', namespace='lab')),
    path('pharmacy/', include('pharmacist.urls', namespace='pharmacy')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
    
=======
from django.templatetags.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include('records.urls', namespace='records')),
    path('employees/', include('employees.urls', namespace='employees'))
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
]
