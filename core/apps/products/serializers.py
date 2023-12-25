from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.thumbnail = validated_data.get(
            'thumbnail', instance.thumbnail)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.image2 = validated_data.get('image2', instance.image2)
        instance.image3 = validated_data.get('image3', instance.image3)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.content = validated_data.get('content', instance.content)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.downloads = validated_data.get(
            'downloads', instance.downloads)
        instance.save()
        return instance
