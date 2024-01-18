from django.shortcuts import render
from django.http import JsonResponse
from .models import Tag
# Create your views here.

def list_tags(request):
    tags = Tag.objects.all()
    tags_data = [{"id": tag.id, "name":tag.label} for tag in tags]
    return JsonResponse({"tags": tags_data})