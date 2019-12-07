from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import get_jadwal_siak

urlpatterns = [
    path('api/jadwal-siak/', get_jadwal_siak, name='jadwal-siak'),
]
