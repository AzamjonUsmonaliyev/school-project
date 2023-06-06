from django.shortcuts import render
from .models import MainImage,About,Card,History,Student ,Testimonials,Partner
from blog.models import Course,Teacher

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
    data={
        'about':About.objects.all(),
        'cards': Card.objects.all()[::2],
        'cards1': Card.objects.all()[1::2],
        'testimoials': Testimonials.objects.all(),
        'partner': Partner.objects.all(),
    }
    return render(request,'about.html',data)


def course(request):

    data={
        'course':Course.objects.all(),
        'star1':[1,2,3,4,5],
        'star2':[1,2,3,4],
        'partner':Partner.objects.all(),
    }
    return render(request ,'course.html',data)

def contact(request):
    return render(request,'contact.html',{'partner':Partner.objects.all()})

def teacher(request):
    data={
        'teachers': Teacher.objects.all(),
        'testimoials': Testimonials.objects.all(),
        'partner': Partner.objects.all(),
    }
    return render(request,'teachers.html',data)