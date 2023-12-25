from django.db import models


class SocialLink(models.Model):
    link = models.CharField(max_length=100, null=True)

    def __self__(self):
        return f'{self.link}'
