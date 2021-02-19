from . import views
from django.urls import path 

urlpatterns = [
    path('medicalpost', views.MedicalPostList.as_view(), name='medical_blog'),
    path('<slug:slug_medi>/', views.MedicalPostDetail.as_view(), name='post_detail_medical'),
]