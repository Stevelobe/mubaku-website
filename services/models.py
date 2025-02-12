from django.db import models

class Training(models.Model):
    # define fields here, e.g.
    name = models.CharField(max_length=100)
    description = models.TextField()
    # other fields as needed
