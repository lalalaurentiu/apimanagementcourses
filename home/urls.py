from django.urls import path, include, re_path
from rest_framework import routers
from .views import programmingCoursesdownload, languageCoursesdownload
from .serializers import admin_programming_courses_viewsets, AdminLanguageCourseViewsets


app_name = "home"

router = routers.DefaultRouter()
router.register(r"programming",admin_programming_courses_viewsets)
router.register(r'language', AdminLanguageCourseViewsets)

urlpatterns = [
    path("download_language/",languageCoursesdownload, name="download_language"),
    path("download_programming/",programmingCoursesdownload, name="download_programming"),
    re_path(r"^", include(router.urls)),
]
