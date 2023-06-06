from django.shortcuts import render
from .models import MainImage,About,Card,History,Student ,Testimonials,Partner

def home(request):
    main_image = MainImage.objects.all()
    about = About.objects.all()
    card = Card.objects.all()
    history = History.objects.all()
    student = Student.objects.all()
    testimoials = Testimonials.objects.all()
    partner = Partner.objects.all()
    data = {
        'main_image':main_image,
        'about':about,
        'cards':card[::2],
        'cards1':card[1::2],
        'history':history,
        'Student':student[0],
        'testimoials':testimoials,
        'partner':partner

    }

    return render(request,'index.html',data)


def about(request):
    return render(request,'about.html')