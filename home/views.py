from django.shortcuts import render
import mimetypes
from silviu.settings import MEDIA_ROOT
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def programmingCoursesdownload(request):
    filename = 'programming_courses.json'
    filepath = MEDIA_ROOT + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

@require_http_methods(["GET"])
def languageCoursesdownload(request):
    filename = 'language_courses.json'
    filepath = MEDIA_ROOT + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
