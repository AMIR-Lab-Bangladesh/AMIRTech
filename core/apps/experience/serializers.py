from rest_framework import serializers
from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get(
            'company_name', instance.company_name)
        instance.job_title = validated_data.get(
            'job_title', instance.job_title)
        instance.from_date = validated_data.get(
            'from_date', instance.from_date)
        instance.to_date = validated_data.get('to_date', instance.to_date)
        instance.save()
        return instance
