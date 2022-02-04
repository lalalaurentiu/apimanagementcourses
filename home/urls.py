
from django.urls import path, include
from rest_framework import routers, viewsets ,status, response, permissions, serializers, renderers
from .models import admin_programming_courses
# from .serializers import admin_programming_courses_serialized
from django.http import FileResponse
from rest_framework.decorators import action
from .views import download


app_name = "home"

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
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return response.Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self, instance, validated_data): 
    #     instance.id = validated_data.get("id", instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
    # @action(methods=['GET'], detail=True)
    # def download(self, request, **kwargs):
    #     att = self.get_object()
    #     file_handle = att.file.open()

    #     mimetype, _ = mimetypes.guess_type(att.file.path)
    #     response = FileResponse(file_handle, content_type=mimetype)
    #     response['Content-Length'] = att.file.size
    #     response['Content-Disposition'] = "attachment; filename={}".format(att.filename)
    #     return response




        

router = routers.DefaultRouter()
router.register("",admin_programming_courses_viewsets)



urlpatterns = [
    path("download/",download, name="download"),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    
]
