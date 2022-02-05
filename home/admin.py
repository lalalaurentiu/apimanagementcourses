from django.contrib import admin
from .models import admin_programming_courses, admin_language_courses

admin.site.register(admin_programming_courses)
admin.site.register(admin_language_courses)
