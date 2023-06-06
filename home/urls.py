from django.urls import path
from .views import home,about,course,contact,teacher

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('course/',course,name='course'),
    path('contact/',contact,name='contact'),
    path('teacher/',teacher,name='teacher'),
]
