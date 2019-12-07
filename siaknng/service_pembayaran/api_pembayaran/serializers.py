from .models import Pembayaran
from rest_framework import serializers


class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = "__all__"