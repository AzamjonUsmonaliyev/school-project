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


