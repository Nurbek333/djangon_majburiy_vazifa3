from django.urls import path
from .views import index,about,blog,contact,services

urlpatterns = [

path('',index,name="home-page"),
path('about/',about,name= "about-page"),
path('blog/',blog,name= "blog-page"),
path('contact/',contact,name= "contact-page"),
path('services/',services,name= "services-page"),
]