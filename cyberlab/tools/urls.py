from django.urls import path
from . import views

urlpatterns = [
    path('base64/', views.base64_tool, name='base64_tool'),
    path('binary/', views.binary_tool, name='binary_tool'),
    path('hex/', views.hex_tool, name='hex_tool'),
    path('url/', views.url_tool, name='url_tool'),
    path('rot13/', views.rot13_tool, name='rot13_tool'),
]
