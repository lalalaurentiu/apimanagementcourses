from django.db import models

level_status  = [
        ("associate", "associate"),
        ("proffessional", "proffessional"),
        ("expert", "expert")
    ]

exam_type_status = [
    ("proiect", "proiect"),
    ("teoretic", "teoretic"),
    ("practic", "practic")
]

class admin_programming_courses(models.Model):

    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    level = models.CharField(max_length=20, choices=level_status)
    exam_type = models.CharField(max_length=20, choices=exam_type_status)

class admin_language_courses(models.Model):

    level_status = [
        ("A1", "A1"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2")
    ]

    nume = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    level = models.CharField(max_length=2,choices=level_status)

