from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image')
    search_fields = ('title', 'content')

admin.site.register(Blog, BlogAdmin)