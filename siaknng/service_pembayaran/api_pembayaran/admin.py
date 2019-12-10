from django.contrib import admin
from .models import Pembayaran


class PembayaranAdmin(admin.ModelAdmin):
    serach_fields = ['npm_mahasiswa',]
    list_display = ['npm_mahasiswa', 'status_pembayaran',]
    list_filter = ['npm_mahasiswa', 'status_pembayaran',]

admin.site.register(Pembayaran, PembayaranAdmin)
