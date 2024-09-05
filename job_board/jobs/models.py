
from django.db import models
from accounts.models import EmployerProfile, CandidateProfile

class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField(default = '')
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(max_length=20, default='full-time')
    requirements = models.TextField(max_length=255, default='')

    def get_requirements_list(self):
        return self.requirements.split(',') if self.requirements else []
    def __str__(self):
        return self.title



class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications',)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='applications/resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
       return f"{self.candidate.user.username} applied for {self.job.title}"
