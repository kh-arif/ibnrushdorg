from django.contrib import admin
from .models import MedicalPost

class MedicalPostAdmin(admin.ModelAdmin):
    list_display = ('title_medi', 'slug_medi', 'status_medi','created_on_medi')
    list_filter = ("status_meid",)
    search_fields = ['title_medi', 'content_medi']
    prepopulated_fields = {'slug_medi': ('title_medi',)}
    
admin.site.register(MedicalPost)