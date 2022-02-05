from dataclasses import fields
from rest_framework import viewsets ,status, response, permissions, serializers
from .models import admin_programming_courses, admin_language_courses


class admin_programming_courses_serialized(serializers.ModelSerializer):

    class Meta:
        model = admin_programming_courses
        fields = ["id","name", "instructor", "start_date", "level" , "exam_type"]

class admin_programming_courses_viewsets(viewsets.ModelViewSet):
    queryset = admin_programming_courses.objects.all()
    serializer_class  = admin_programming_courses_serialized
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(admin_programming_courses.objects.all()) < 15:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return response.Response({"msg":"prea multe"}, status=status.HTTP_400_BAD_REQUEST)

class AdminLanguageCourseSerialized(serializers.ModelSerializer):
    
    class Meta:
        model = admin_language_courses
        fields = ["id", "nume", "instructor", "start_date", "level"]

class AdminLanguageCourseViewsets(viewsets.ModelViewSet):
    queryset = admin_language_courses.objects.all()
    serializer_class = AdminLanguageCourseSerialized
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if len(admin_language_courses.objects.all()) < 15:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return response.Response({"msg":"prea multe"}, status=status.HTTP_400_BAD_REQUEST)