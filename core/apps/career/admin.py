from django.contrib import admin

from .models import Career


class CareerAdmin(admin.ModelAdmin):
    model = Career
    list_display = ['title', 'department', 'location',
                    'salary', 'description', 'thumbnail']


admin.site.register(Career, CareerAdmin)
