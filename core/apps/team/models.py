from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    profile_pic = models.ImageField(
        upload_to='profile_pic/Team', null=True, blank=True)
    # this is will be foreign key
    designation = models.CharField(max_length=100, null=True)
    seniority = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)  # fk
    education = models.CharField(max_length=100, null=True)  # fk
    social_link = models.CharField(max_length=100, null=True)  # fk

    def __str__(self):
        return f'{self.name, self.designation, self.about, self.profile_pic, self.seniority, self.email, self.phone, self.address, self.experience, self.education, self.social_link}'
