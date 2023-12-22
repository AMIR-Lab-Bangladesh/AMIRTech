from django.db import models

# Create your models here.


class Experience(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    job_title = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    def __self__(self):
        return f'{self.company_name, self.job_title, self.from_date, self.to_date}'
