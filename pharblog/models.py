from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = (
    (0,"Drafst"),
    (1,"Publish")
)

class PharPost(models.Model):
    title_phar = models.CharField(max_length=200, unique=True)
    slug_phar = models.SlugField(max_length=200, unique=True)
    author_phar = models.ForeignKey(User, on_delete=models.CASCADE,related_name='phar_blog_posts')
    updated_on_phar = models.DateTimeField(default = timezone.now)
    content_phar = models.TextField()
    created_on_phar =models.DateTimeField(default = timezone.now)
    status_phar = models.IntegerField(choices=STATUS, default=0)
    image_phar = models.ImageField(default ='default.jpg', upload_to ='medical/media/image-pics')



class Meta:
    ordering =['-created_on_phar']

def __str__(self):
    return self.title_phar