from django.db import models

class Course(models.Model):
    image = models.FileField(upload_to="course/image")
    title = models.CharField(max_length=200)
    text = models.TextField()
    star = models.FloatField()
    month = models.PositiveSmallIntegerField()
    student = models.PositiveSmallIntegerField()
    books = models.PositiveSmallIntegerField()