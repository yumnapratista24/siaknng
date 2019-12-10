from django.db import models

class Pembayaran(models.Model):
    npm_mahasiswa = models.CharField(max_length=10, unique=True)
    status_pembayaran = models.BooleanField(default=False)

    def __str__(self):
        return self.npm_mahasiswa
    