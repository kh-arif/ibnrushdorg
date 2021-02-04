from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = (
    (0,"Drafst"),
    (1,"Publish")
)

class MedicalPost(models.Model):
    title_medi = models.CharField(max_length=200, unique=True)
    slug_medi = models.SlugField(max_length=200, unique=True)
    author_medi = models.ForeignKey(User, on_delete=models.CASCADE,related_name='medical_blog_posts')
    updated_on_medi = models.DateTimeField(default = timezone.now)
    content_medi = models.TextField()
    created_on_medi =models.DateTimeField(default = timezone.now)
    status_medi = models.IntegerField(choices=STATUS, default=0)
    image_medi = models.ImageField(default ='default.jpg', upload_to ='medical/media/image-pics')



class Meta:
    ordering =['-created_on_medi']

def __str__(self):
    return self.title_medi