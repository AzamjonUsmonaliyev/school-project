from django.shortcuts import render

from .models import Category,Post
from home.models import Partner

def blog(request):
    data ={
        'post':Post.objects.all(),
        'partner':Partner.objects.all(),
    }
    return render(request,'blog.html',data)

def singleblog(request,id):
    return render(request,'blog-single.html')


