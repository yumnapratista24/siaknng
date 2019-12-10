from django.db import models
from datetime import datetime

class JadwalSiak(models.Model):
    id_fakultas = models.IntegerField(default=0, unique=True)
    nama_fakultas = models.CharField(max_length=20, default="Tidak ada")
    status_jadwal = models.BooleanField(default=False)

    class Meta:
        ordering=['id_fakultas','nama_fakultas']

    def __str__(self):
        return '{}'.format(self.id_fakultas)
