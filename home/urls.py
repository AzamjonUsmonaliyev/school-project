from django.urls import path
from .views import home,blog

urlpatterns = [
    path('home/',home,name='home'),
    path('blog/',blog,name='blog'),
]
