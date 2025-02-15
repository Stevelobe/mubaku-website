from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('send-message/', views.contacts, name='send_message'),
    path('funding/', views.funding, name='funding'),
    path('training/', views.training_view, name='training'),  
    path('training/business/', views.business_training, name='business_training'),
    path('training/tech/', views.tech_training, name='tech_training'),
    path('training/leadership/', views.leadership_training, name='leadership_training'),
]
