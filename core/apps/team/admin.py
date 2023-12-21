from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'profile_pic', 'designation', 'seniority',
                    'email', 'phone', 'address', 'experience', 'education', 'social_link')
    search_fields = ('name', 'about', 'profile_pic', 'designation', 'seniority',
                     'email', 'phone', 'address', 'experience', 'education', 'social_link')
    readonly_fields = ('id',)
