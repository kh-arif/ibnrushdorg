from . import views
from django.urls import path 

urlpatterns = [
    path('medicalpost', views.MedicalPostList.as_view(), name='medica_blog'),
]


