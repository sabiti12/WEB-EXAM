from . import views
from django.urls import path

urlpatterns = [
    path('', views.guest,name="index"),
    path('contact', views.contact,name="contact"),

]