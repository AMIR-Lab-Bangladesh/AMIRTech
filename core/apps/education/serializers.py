from rest_framework import serializers
from .models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

    def update(self, validated_data):
        instance = self.instance
        instance.institute_name = validated_data.get(
            'institute_name', instance.institute_name)
        instance.degree = validated_data.get(
            'degree', instance.degree)
        instance.from_date = validated_data.get(
            'from_date', instance.from_date)
        instance.to_date = validated_data.get('to_date', instance.to_date)
        instance.save()
        return instance
