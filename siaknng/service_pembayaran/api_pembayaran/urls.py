from .views import get_pembayaran_siak
from django.urls import path

urlpatterns = [
    path('api/pembayaran-siak/', get_pembayaran_siak, name='pembayaran-siak'),
]
