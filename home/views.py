from django.shortcuts import render
import mimetypes
from silviu.settings import MEDIA_ROOT
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def download(request):
    # Define text file name
    filename = 'file.json'
    # Define the full file path
    filepath = MEDIA_ROOT + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
