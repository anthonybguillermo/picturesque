from django.contrib import admin
from django.urls import path
from . import views
from .views import our_story, contact_us, faqs

urlpatterns = [
    path('', views.home, name='home'),
    path('our_story/', our_story, name="our_story"),
    path('contact_us/', contact_us, name="contact_us"),
    path('faqs/', faqs, name="faqs"),
]