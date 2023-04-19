from django.db import models

class Course(models.Model):
    image = models.FileField(upload_to="course/image")
    title = models.CharField(max_length=200)
    text = models.TextField()
    star = models.FloatField()
    month = models.PositiveSmallIntegerField()
    student = models.PositiveSmallIntegerField()
    books = models.PositiveSmallIntegerField()

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    month =models.PositiveSmallIntegerField()
    test =models.CharField(max_length=256)
    icon = models.CharField(max_length=70)
    disk = models.PositiveSmallIntegerField(default=50)
    email = models.PositiveSmallIntegerField(default=50)
    bandwidth = models.PositiveSmallIntegerField(default=50)
    subdomain = models.PositiveSmallIntegerField(default=10)
    domain = models.PositiveSmallIntegerField(default=50)
