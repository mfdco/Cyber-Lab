from django.urls import path
from . import views

urlpatterns = [
    path('base64/', views.base64_tool, name='base64_tool'),
    path('binary/', views.binary_tool, name='binary_tool'),
]
