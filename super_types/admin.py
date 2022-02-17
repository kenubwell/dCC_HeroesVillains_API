#(5 points) As a developer, I want to register the SuperTypes model with the admin site so I can:
# Register a new super user (python manage.py createsuperuser) | Visit the admin site | Seed two values (“Hero” and “Villain”) into the “super_type” table

from django.contrib import admin
from .models import SuperTypes

admin.site.register(SuperTypes) #this will permit Admin Center interface with our database/table