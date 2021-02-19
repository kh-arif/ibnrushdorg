from django.views import generic
from django.shortcuts import render
from .models import MedicalPost
# Create your views here.

class MedicalPostList(generic.ListView):
    queryset = MedicalPost.objects.filter(status_medi=1).order_by('-created_on_medi')
    template_name = 'medical_blog.html'


class MedicalPostDetail(generic.DetailView):
    model = MedicalPost
    template_name = 'post_detail_medical.html'