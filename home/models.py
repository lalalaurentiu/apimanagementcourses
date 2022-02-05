from django.db import models

programming_level_status  = [
        ("associate", "associate"),
        ("proffessional", "proffessional"),
        ("expert", "expert")
    ]

programming_exam_type_status = [
    ("proiect", "proiect"),
    ("teoretic", "teoretic"),
    ("practic", "practic")
]

class admin_programming_courses(models.Model):

    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    level = models.CharField(max_length=20, choices=programming_level_status)
    exam_type = models.CharField(max_length=20, choices=programming_exam_type_status)

    def __str__(self):
        return self.name

language_level_status = [
    ("A1", "A1"),
    ("B1", "B1"),
    ("B2", "B2"),
    ("C1", "C1"),
    ("C2", "C2")
]

class admin_language_courses(models.Model):

    nume = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    level = models.CharField(max_length=2,choices=language_level_status)

    def __str__(self):
        return self.name

