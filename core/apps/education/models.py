from django.db import models


class Education(models.Model):
    institute_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    def __self__(self):
        return f'{self.institute_name, self.degree, self.from_date, self.to_date}'
