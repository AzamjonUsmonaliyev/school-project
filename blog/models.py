from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    fullname = models.CharField(max_length=200)
    profession = models.CharField(max_length=150)
    facebook = models.URLField(blank=True, null=True)
    duo = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)


class Post(models.Model):
    image = models.ImageField(upload_to='blog/image/')
    title = models.CharField(max_length=250)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.PositiveIntegerField(default=0)
    new =models.BooleanField(default=True)
    note = models.TextField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    opinion = models.TextField(verbose_name='Teacher opinion')

class Cantact(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=30)
    docs = models.TextField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()

class Course(models.Model):
    image = models.FileField(upload_to="course/image")
    title = models.CharField(max_length=200)
    text = models.TextField()
    star = models.FloatField()
    month = models.PositiveSmallIntegerField()
    student = models.PositiveSmallIntegerField()
    books = models.PositiveSmallIntegerField()

