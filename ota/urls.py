from django.urls import path
from . import views

urlpatterns = [
    path('upload_firmware/', views.upload_firmware, name='upload_firmware'),
    path('check_for_updates/', views.check_for_updates, name='check_for_updates'),
    path('firmware_list/', views.firmware_list, name='firmware_list'),
]