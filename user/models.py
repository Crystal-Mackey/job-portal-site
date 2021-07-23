from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = [
('1', 'Job Seeker'),
('2', 'Employer')
]

class User(AbstractUser):
    name = models.CharField(max_length=200)
    skills = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True)
    employee = models.CharField(choices=CHOICES, blank=True, null=True, max_length=1)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
