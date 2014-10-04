from django.contrib import admin
from blogpost.models import BlogPost


class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']

admin.site.register(BlogPost, BlogpostAdmin)