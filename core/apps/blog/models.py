from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(
        upload_to='thumbnail/Blog', null=True, blank=True)
    content = models.TextField()
    tags = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title, self.thumbnail, self.content, self.tags, self.slug, self.views}'
