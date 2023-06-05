from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    faculty = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)