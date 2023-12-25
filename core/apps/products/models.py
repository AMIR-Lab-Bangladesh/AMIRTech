from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    thumbnail = models.ImageField(
        upload_to='thumbnail/products', null=True, blank=True)
    image1 = models.ImageField(
        upload_to='image1/products', null=True, blank=True)
    image2 = models.ImageField(
        upload_to='image2/products', null=True, blank=True)
    image3 = models.ImageField(
        upload_to='image3/products', null=True, blank=True)
    tags = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    slug = models.CharField(max_length=100)
    downloads = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title, self.thumbnail, self.image1, self.image2, self.image3, self.tags, self.content, self.slug, self.downloads}'
