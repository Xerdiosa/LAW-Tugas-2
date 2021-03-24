from django.urls import path
from . import views

urlpatterns = [
    path('filestorage/', views.filestorage),
]
