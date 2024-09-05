
from django import forms
from .models import Job
from .models import Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'job_type', 'requirements']  

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}))
    # employer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}))
    job_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'job type'}))
    application_deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    requirements = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'job requirements'}))


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']

    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Cover Letter',
            'rows': 5
        })
    )
    resume = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )