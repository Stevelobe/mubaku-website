from django.shortcuts import render, get_object_or_404
from .models import Training

def enroll_training(request, id):
    # Get the training object based on the provided ID
    training = get_object_or_404(Training, id=id)

    # Here, you can add logic to handle the enrollment process
    # For now, we will simply pass the training object to the template

    context = {
        'training': training
    }

    return render(request, 'services/enroll_training.html', context)

def services(request):
    return render(request, 'services/services.html')

def tech_fintech(request):
    return render(request, 'services/tech_fintech.html')

def consultancy(request):
    return render(request, 'services/consultancy.html')

def training_detail(request, training_name):
    # Example context (you can fetch real data later)
    context = {
        'training_name': training_name,
        'details': f"Details about the {training_name} training will go here.",
    }
    return render(request, 'services/training_detail.html', context)

def real_estate(request):
    return render(request, 'services/real_estate.html')

def business_tech_school(request):
    """View for the Business Tech School page."""
    trainings = {
        'entrepreneurship': {
            'title': 'Entrepreneurship',
            'price': 'FCFA200,000',
            'location': 'Yaoundé, Cameroon',
            'duration': '4 Months',
            'description': 'Learn how to create and manage successful businesses.',
        },
        'mindset-development': {
            'title': 'Mindset Development and Transformation',
            'price': 'FCFA100,000',
            'location': 'Douala, Cameroon',
            'duration': '3 Months',
            'description': 'Develop skills for personal growth and transformation.',
        },
        'cloud-architecture': {
            'title': 'Cloud Architecture',
            'price': 'FCFA800,000',
            'location': 'Limbe, Cameroon',
            'duration': '6 Months',
            'description': 'Master cloud computing concepts and scalable solution designs.',
        },
    }
    return render(request, 'services/business_tech_school.html', {'trainings': trainings})


def agribusiness(request):
    return render(request, 'services/agribusiness.html')

def ai_solutions(request):
    return render(request, 'services/ai_solutions.html')
