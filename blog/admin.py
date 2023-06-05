from django.contrib import admin
from .models import Category,Cantact,Teacher,Post,Course


admin.site.register([Cantact,Category,Teacher,Post,Course])

# Register your models here.
