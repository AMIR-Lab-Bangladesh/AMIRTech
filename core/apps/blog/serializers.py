from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.thumbnail = validated_data.get(
            'thumbnail', instance.thumbnail)
        instance.content = validated_data.get('content', instance.content)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.views = validated_data.get('views', instance.views)
        instance.save()
        return instance
