from django.contrib import admin
from .models import Post


admin.site.site_header = 'Rushd Administration'
admin.site.site_title = 'Rushd Admin Area'
admin.site.index_title = 'Rushd Admin'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post)