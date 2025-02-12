from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


def home(request):
    print("MEDIA_ROOT: ", settings.MEDIA_ROOT)  # Debugging media directory path
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


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
