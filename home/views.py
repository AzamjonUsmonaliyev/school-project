from django.shortcuts import render
from .models import *

def home(request):
    main_image = MainImage.objects.all()
    about = About.objects.all()

    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')