from django.db import models
from django.contrib.auth.models import AbstractUser


CHOICES = [
('1', 'Looking for a job'),
('2', 'Posting job listings')
]

class User(AbstractUser):
    name = models.CharField(max_length=200)
    skills = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    contact_num = models.IntegerField(null=True, blank=True)
    employee = models.CharField(choices=CHOICES, blank=True, null=True, max_length=1)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
