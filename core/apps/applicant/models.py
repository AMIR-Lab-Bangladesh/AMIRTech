from django.db import models


class Application(models.Model):
    career = models.ForeignKey('career.Career', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    cv = models.FileField(upload_to='cv/', null=True)
    linkedin_profile = models.CharField(max_length=100, null=True)
    github_profile = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.first_name, self.last_name, self.email, self.phone, self.cv, self.linkedin_profile, self.github_profile, self.website}'
