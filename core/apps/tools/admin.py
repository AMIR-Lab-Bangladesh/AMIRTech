from django.contrib import admin

from .models import Tools


class ToolsAdmin(admin.ModelAdmin):
    model = Tools
    list_display = ['title', 'thumbnail', 'image1', 'image2',
                    'image3', 'tags', 'content', 'slug', 'downloads']


admin.site.register(Tools, ToolsAdmin)
