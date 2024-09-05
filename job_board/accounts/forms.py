
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from .models import CandidateProfile,EmployerProfile

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password1', 'password2']
        
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )

class EmployerSignUpForm(UserSignUpForm):
    company_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'})
    )
    company_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Description', 'rows': 4})
    )
    company_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Company URL'})
    )

    class Meta(UserSignUpForm.Meta):
        fields =  ['company_name', 'company_description', 'company_url'] + UserSignUpForm.Meta.fields 


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'bio']
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'multiple': False}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_website', 'company_description']
        widgets = {
            'company_description': forms.Textarea(attrs={'rows': 4}),
        }