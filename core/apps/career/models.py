from django.db import models


class Career(models.Model):
    title = models.ForeignKey(
        'designation.Designation', related_name='career_designation',  on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=255, null=True)
    location = models.BooleanField(null=True)
    salary = models.FloatField(null=True)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(
        upload_to='career/thumbnail', null=True, blank=True)

    def __str__(self):
        return f'{self.title, self.department, self.location, self.salary, self.description, self.thumbnail}'
