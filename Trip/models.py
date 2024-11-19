from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
User = get_user_model()
# Create your models here.

#trips & #notes table

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2) #NG, UK, US
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'trips')
    #to allow only users who log in(people who start a trip)we want them to be the owner of that trip(we will be using user authentication)

    def __str__(self):
        return self.city

class Note(models.Model):
    EXCURSIONS = (
        ('event', 'Event'),
        ('dining', 'Dining'),
        ('experience', 'Experience'),
        ('general', 'General'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'notes')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices = EXCURSIONS)
    img = models.ImageField(upload_to='notes', blank=True, null=True)#upload_to='notes' will create a notes directory
    #blank = True, null=True means adding that particular model is not compulsory
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} in {self.trip.city}"