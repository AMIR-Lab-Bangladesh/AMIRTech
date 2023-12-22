from rest_framework import serializers
from .models import Career

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.department = validated_data.get('department', instance.department)
        instance.location = validated_data.get('location', instance.location)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.description = validated_data.get('description', instance.description)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.save()
        return instance
