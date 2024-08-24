import datetime
import os
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image, Service
from django.core.files.storage import default_storage
from django.conf import settings
from .serializers import ImageSerializer,ServiceSerializer
# Create your views here.




