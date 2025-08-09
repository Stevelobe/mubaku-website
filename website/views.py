from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Enrollment
from .models import IncubatorApplication, Workshops



def home(request):
    print("MEDIA_ROOT: ", settings.MEDIA_ROOT)  # Debugging media directory path
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')

def funding(request):
    return render(request, 'funding.html')

def boot_camp(request):
    return render(request, "training/boot_camp.html")

def enroll_user(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        program = request.POST.get('program')

        Enrollment.objects.create(full_name=full_name, email=email, phone=phone, program=program)
        messages.success(request, "Enrollment successful! We will contact you soon.")
        return redirect('boot_camp')  # Change this to your bootcamp page name

    return redirect('boot_camp')

def bootcamp_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        program = request.POST.get('program')

        # Save the data into the database
        enrollment = Enrollment.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            program=program
        )
        
        # Display a success message
        messages.success(request, "Your registration was successful! We will contact you soon.")
        
        return redirect('boot_camp')  # Redirect back to the workshops page after saving
        
    return redirect('boot_camp')

def workshop_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        workshops = request.POST.get('workshops')

        # Save the data into the database
        enrollment = Workshops.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            workshops=workshops
        )
        
        # Display a success message
        messages.success(request, "Your registration was successful! We will contact you soon.")
        
        return redirect('workshops')  # Redirect back to the workshops page after saving
        
    return redirect('workshops')



def incubator_apply(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        business_idea = request.POST.get('business_idea')

        # Save the application data in the database
        IncubatorApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            business_idea=business_idea
        )

        # Send a success message
        messages.success(request, "Your application has been received! We will contact you soon.")
        return redirect('incubators')  # Redirect back to the incubators page

    return redirect('incubators')

def seminars(request):
    return render(request, "training/seminars.html")

def workshops(request):
    return render(request, "training/workshops.html")

def incubators(request):
    return render(request, "training/incubators.html")

def contacts(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Debugging: print received data to the console
        print(f"Message Received:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        # Simulate message handling (e.g., send email or save to the database)
        messages.success(request, "Your message has been sent successfully! We will get back to you shortly.")
        
        # Redirect to the homepage after the form submission
        return redirect('home')  # Redirect to the homepage or another page as needed

    # If it's a GET request, render the contact form
    return render(request, 'contacts.html')
