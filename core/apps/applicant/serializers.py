from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.career = validated_data.get('career', instance.career)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.cv = validated_data.get('cv', instance.cv)
        instance.linkedin_profile = validated_data.get('linkedin_profile', instance.linkedin_profile)
        instance.github_profile = validated_data.get('github_profile', instance.github_profile)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance
