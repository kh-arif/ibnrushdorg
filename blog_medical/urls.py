from . import views
from django.urls import path 

urlpatterns = [
    path('medicalpost', views.MedicalPostBlog, name='medica_blog'),
]


