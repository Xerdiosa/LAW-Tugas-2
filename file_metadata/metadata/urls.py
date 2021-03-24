from django.urls import path
from . import views

urlpatterns = [
    path('metadata/', views.MetadataView.as_view()),
]
