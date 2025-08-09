from django.db import models

class Enrollment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    program = models.CharField(max_length=255)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.program}"

class IncubatorApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    business_idea = models.TextField()

    def __str__(self):
        return self.full_name
    
class Workshops(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    workshops = models.CharField(max_length=255)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.workshops}"