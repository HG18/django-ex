import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    str="Hello Word"

    return str

def health(request):
    return HttpResponse(PageView.objects.count())
