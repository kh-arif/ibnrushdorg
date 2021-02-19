from django.views import generic
from django.shortcuts import render
from .models import PharPost
# Create your views here.

class PharPostList(generic.ListView):
    queryset = PharPost.objects.filter(status_phar=1).order_by('-created_on_phar')
    template_name = 'phar_blog.html'


class PharPostDetail(generic.DetailView):
    model = PharPost
    template_name = 'post_detail_phar.html'