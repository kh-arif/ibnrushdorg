from . import views
from django.urls import path 

urlpatterns = [
    path('medicalpost', views.MedicalPostList, name='medica_blog'),
]


