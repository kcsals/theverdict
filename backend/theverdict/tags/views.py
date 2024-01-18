from django.shortcuts import render
from django.http import JsonResponse
from .models import Tag
# Create your views here.

def list_tags(request):
    tags = Tag.objects.get(pk=1)
    print("This is-----------------------------------------------------------:", tags)