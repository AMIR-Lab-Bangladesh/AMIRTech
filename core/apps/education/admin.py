from django.contrib import admin

from .models import Education


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = ['institute_name', 'degree', 'from_date', 'to_date']


admin.site.register(Education, EducationAdmin)
