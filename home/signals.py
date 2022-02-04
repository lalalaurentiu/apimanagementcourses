from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from silviu.settings import MEDIA_ROOT
from .models import admin_programming_courses
import json

@receiver(post_save, sender=admin_programming_courses)
def download(sender, instance, created, **kwargs):
    data = admin_programming_courses.objects.all()
    lst = []
    if created:
        for i in data:
            lst.append({
                "id":i.id,
                "name":i.name,
                "instructor":i.instructor,
                "start_date":str(i.start_date),
                "level":i.level,
                "exam_type":i.exam_type
            })
    print(lst)
    jsonfile = json.dumps(lst)
    with open(f"{MEDIA_ROOT}/file.json", "w") as file:
        file.write(jsonfile)
