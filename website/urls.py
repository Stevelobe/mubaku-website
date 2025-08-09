from django.urls import path
from . import views
from .views import enroll_user

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('send-message/', views.contacts, name='send_message'),
    path('funding/', views.funding, name='funding'),  
    path("training/boot-camp/", views.boot_camp, name="boot_camp"),
    path("training/seminars/", views.seminars, name="seminars"),
    path("training/workshops/", views.workshops, name="workshops"),
    path("training/incubators/", views.incubators, name="incubators"),
    path('enroll/', enroll_user, name='enroll'),
    path('workshop/register/', views.workshop_register, name='workshop_register'),
    path('bootcamp/register/', views.bootcamp_register, name='bootcamp_register'),
    
    path('apply/incubator/', views.incubator_apply, name='incubator_apply'),
]
