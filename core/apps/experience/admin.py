from django.contrib import admin


from .models import Experience


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = ['company_name', 'job_title', 'from_date', 'to_date']


admin.site.register(Experience, ExperienceAdmin)
