from rest_framework import serializers, response, status
from .models import admin_programming_courses, level_status, exam_type_status

class admin_programming_courses_serialized(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100)
    instructor = serializers.CharField(max_length = 100)
    start_date = serializers.DateField()
    level = serializers.ChoiceField(choices=level_status)
    exam_type = serializers.ChoiceField(choices=exam_type_status)

    def create(self, validated_data):

        return admin_programming_courses.objects.create(**validated_data)

