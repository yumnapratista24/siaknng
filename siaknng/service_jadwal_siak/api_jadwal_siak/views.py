from django.http.response import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import JadwalSiak
from .serializers import JadwalSiakSerializer
import json

'''
Views of Django Rest API using function api_view
@csrf_exempt applied for only development, to bypass CROSS ORIGIN
Input dari Model Admin
'''
@csrf_exempt
@api_view(["GET"])
def get_jadwal_siak(request):
    jadwal_siak = JadwalSiak.objects.all()
    jadwal_siak_serializers = JadwalSiakSerializer(jadwal_siak, many=True)
    return Response(jadwal_siak_serializers.data)

