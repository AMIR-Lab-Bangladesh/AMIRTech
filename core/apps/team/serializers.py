from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.profile_pic = validated_data.get(
            'profile_pic', instance.profile_pic)
        instance.designation = validated_data.get(
            'designation', instance.designation)
        instance.seniority = validated_data.get(
            'seniority', instance.seniority)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.experience = validated_data.get(
            'experience', instance.experience)
        instance.education = validated_data.get(
            'education', instance.education)
        instance.social_link = validated_data.get(
            'social_link', instance.social_link)
        instance.save()
        return instance
