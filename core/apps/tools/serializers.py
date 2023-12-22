from rest_framework import serializers
from .models import Tools


class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = ['title', 'thumbnail', 'image1', 'image2',
                  'image3', 'tags', 'content', 'slug', 'downloads']

    def update(seld, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
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
