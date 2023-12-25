from django.contrib import admin

from .models import Designation


class DesignationAdmin(admin.ModelAdmin):
    model = Designation
    list_display = ['title']


admin.site.register(Designation, DesignationAdmin)
