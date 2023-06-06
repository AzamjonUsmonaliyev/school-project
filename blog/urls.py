from django.urls import path
from .views import blog,singleblog

urlpatterns = [
    path('',blog,name='blog'),
    path('<int:id>/',singleblog,name='singleblog'),

]