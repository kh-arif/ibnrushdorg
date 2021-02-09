from django.views import generic
from django.shortcuts import render
from .models import MedicalPost
# Create your views here.

class MedicalPostList(generic.ListView):
    queryset = MedicalPost
    template_name = 'medical_blog.html'


class MedicalPostDetail(generic.DetailView):
    model = MedicalPost
    template_name = 'medical_post_detail.html'