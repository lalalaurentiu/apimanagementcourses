from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from management.settings import MEDIA_ROOT
from .models import admin_programming_courses, admin_language_courses
import json

@receiver(post_save, sender=admin_programming_courses)
@receiver(post_delete, sender=admin_programming_courses)
def progarmmingDownload(sender, instance, created=None, **kwargs):
    data = admin_programming_courses.objects.all()
    lst = []
    if created or instance:
        for i in data:
            lst.append({
                "id":i.id,
                "name":i.name,
                "instructor":i.instructor,
                "start_date":str(i.start_date),
                "level":i.level,
                "exam_type":i.exam_type
            })

    jsonfile = json.dumps(lst,indent=4, sort_keys=True)
    with open(f"{MEDIA_ROOT}/programming_courses.json", "w") as file:
        file.write(jsonfile)

@receiver(post_save, sender=admin_language_courses)
@receiver(post_delete, sender=admin_language_courses)
def progarmmingDownload(sender, instance, created=None, **kwargs):
    data = admin_language_courses.objects.all()
    lst = []
    if created or instance:
        for i in data:
            lst.append({
                "id":i.id,
                "name":i.nume,
                "instructor":i.instructor,
                "start_date":str(i.start_date),
                "level":i.level
            })

    jsonfile = json.dumps(lst ,indent=4, sort_keys=True)
    with open(f"{MEDIA_ROOT}/language_courses.json", "w") as file:
        file.write(jsonfile)
