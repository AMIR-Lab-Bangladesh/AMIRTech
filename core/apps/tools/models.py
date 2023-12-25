from django.db import models


class Tools(models.Model):
    title = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(
        upload_to='thumbnail/Tools', null=True, blank=True)
    image1 = models.ImageField(upload_to='image1/Tools', null=True, blank=True)
    image2 = models.ImageField(upload_to='image2/Tools', null=True, blank=True)
    image3 = models.ImageField(upload_to='image3/Tools', null=True, blank=True)

    tags = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    slug = models.CharField(max_length=100)
    downloads = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title, self.thumbnail, self.image1, self.image2, self.image3, self.tags, self.content, self.slug, self.downloads}'
