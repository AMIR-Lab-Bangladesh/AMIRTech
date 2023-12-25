from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='cart_user', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(
        'products.Product', related_name='cart_product', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username, self.product.title }'
