from rest_framework import serializers
from .models import Designation


class DesignationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
