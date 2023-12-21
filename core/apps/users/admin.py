from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_staff', 'is_active',
                    'is_superuser', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)
