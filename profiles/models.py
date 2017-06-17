from django.db import models


# Create your models here.


# creates the model for the profile page
class profile(models.Model):
    # creates a name variable with no more than 120 chars
    name = models.CharField(max_length=120)
    # by setting null true it doesn't have to have a value in the database.
    description = models.TextField(default='Add a description')


# in python 3 use str not unicode
    def __str__(self):
        return self.name
