from . import views
from django.urls import path

urlpatterns = [
    path('', views.guest,name="index"),
    path('contact', views.contact,name="contact"),
    path('speakers',views.speakers,name="speakers"),
    path('about',views.about,name="about-us"),
    path('schedule',views.schedule,name="schedule"),
    path('sponsors',views.sponsors,name="sponsors"),




]