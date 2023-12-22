from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'profile_pic', 'seniority',
                    'email', 'phone', 'address')
    search_fields = ('name', 'about', 'profile_pic', 'seniority',
                     'email', 'phone', 'address')
    readonly_fields = ('id',)
