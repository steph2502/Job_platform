from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    resume = models.FileField(upload_to='resumes/',blank=True, null=True)
    bio = models.TextField()
    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    company_website = models.URLField()
    company_description = models.TextField()
    def __str__(self):
        return self.company_name

