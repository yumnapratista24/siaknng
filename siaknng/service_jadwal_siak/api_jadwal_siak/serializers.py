from rest_framework import serializers
from .models import JadwalSiak

class JadwalSiakSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalSiak
        fields = "__all__"
