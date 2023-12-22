from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ['title', 'thumbnail',
                    'tags', 'content', 'slug', 'views']


admin.site.register(Blog, BlogAdmin)
