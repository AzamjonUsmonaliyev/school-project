from django.db import models

class MainImage(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='about/image/main/')

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=250,blank=True,null=True)
    text = models.TextField()
    createdata = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Card(models.Model):
    image = models.ImageField(upload_to='about/image/cart/')
    title =models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
class History(models.Model):
    year = models.PositiveSmallIntegerField()
    text =models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.year}"


class Student(models.Model):
    student = models.IntegerField(default=12000)
    course = models.IntegerField(default=240)
    year = models.PositiveSmallIntegerField(default=55)

    def __str__(self):
        return f"{self.student}"


class Testimonials(models.Model):
    fullname=models.CharField(max_length=150)
    image = models.ImageField(upload_to='about/image/tester')
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.fullname

class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/image/partner/')

    def __str__(self):
        return self.name

