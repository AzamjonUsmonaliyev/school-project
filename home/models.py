from django.db import models

class About(models.Model):
    title = models.CharField(max_length=250,blank=True,null=True)
    text = models.TextField()
    createdata = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    year = models.PositiveSmallIntegerField()
    text =models.TextField()
    image = models.ImageField()

