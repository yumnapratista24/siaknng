from django.contrib import admin
from .models import JadwalSiak

class JadwalSiakAdmin(admin.ModelAdmin):
  search_fields = ['id_fakultas', 'nama_fakultas',]
  list_display = ('id_fakultas', 'nama_fakultas','status_jadwal',)
  list_filter = ('id_fakultas', 'nama_fakultas',)

# Init register admin models
admin.site.register(JadwalSiak, JadwalSiakAdmin)