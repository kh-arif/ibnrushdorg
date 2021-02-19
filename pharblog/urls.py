from . import views
from django.urls import path 

urlpatterns = [
    path('postphar', views.PharPostList.as_view(), name='phar_blog'),
    path('<slug:slug_phar>/', views.PharPostDetail.as_view(), name='post_detail_phar'),

]