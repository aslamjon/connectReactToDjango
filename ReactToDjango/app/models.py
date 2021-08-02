from django.db import models

class Student(models.Model):
    name = models.TextField()
    des = models.TextField()
