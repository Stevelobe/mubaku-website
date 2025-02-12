from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('tech-fintech/', views.tech_fintech, name='tech_fintech'),
    path('consultancy/', views.consultancy, name='consultancy'),
    path('real-estate/', views.real_estate, name='real_estate'),
    path('business-tech-school/', views.business_tech_school, name='business_tech_school'),
    path('agribusiness/', views.agribusiness, name='agribusiness'),
    path('ai-solutions/', views.ai_solutions, name='ai_solutions'),
    path('training/<str:training_name>/', views.training_detail, name='training_detail'),
    path('training/enroll/<int:id>/', views.enroll_training, name='enroll_training'),
]
