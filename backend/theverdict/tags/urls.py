from django.urls import path
from . import views

urlpatterns = [
    path('list_tags/', views.list_tags, name='list_tags'),
]
