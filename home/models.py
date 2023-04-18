from django.db import models

class MainImage(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='about/image/main/')

class About(models.Model):
    title = models.CharField(max_length=250,blank=True,null=True)
    text = models.TextField()
    createdata = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    year = models.PositiveSmallIntegerField()
    text =models.TextField()
    image = models.ImageField()


class Student(models.Model):
    student = models.IntegerField(default=12000)
    course = models.IntegerField(default=240)
    year = models.PositiveSmallIntegerField(default=55)

class Plan(models.Model):
    CHOICE  =(
        ('PRE MONTH','PRE MONTH'),
        ('YEAR','YEAR'),
    )
    price = models.PositiveIntegerField(default=30)
    period =models.CharField(choices=CHOICE,max_length=30)
    emailaddres =models.PositiveSmallIntegerField(default=150)
    storage = models.PositiveSmallIntegerField(default=65)
    database =models.PositiveSmallIntegerField(default=45)
    domain = models.PositiveSmallIntegerField(default=27)
    support =models.CharField(max_length=30)

class Testimonials(models.Model):
    fullname=models.CharField(max_length=150)
    image = models.ImageField(upload_to='about/image/tester')
    title = models.CharField(max_length=200)
    text = models.TextField()

class Partner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/image/partner/')


