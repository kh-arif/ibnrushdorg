from django.contrib import admin
from .models import PharPost


class PharPostAdmin(admin.ModelAdmin):
    list_display = ('title_phar', 'slug_phar', 'status_phar','created_on_phar')
    list_filter = ("status_phar",)
    search_fields = ['title_phar', 'content_phar']
    prepopulated_fields = {'slug_phar': ('title_phar',)}
    
admin.site.register(PharPost)