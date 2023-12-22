from django.contrib import admin

from .models import SocialLink


class SocialAdmin(admin.ModelAdmin):
    model = SocialLink
    list_display = ['link']


admin.site.register(SocialLink, SocialAdmin)
