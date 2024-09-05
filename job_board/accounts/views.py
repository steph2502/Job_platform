
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm,UserSignUpForm,CandidateProfileForm,EmployerProfileForm,EmployerSignUpForm,CandidateProfile,EmployerProfile

@login_required
def profile(request):
    if request.user.is_candidate:
        profile = request.user.candidate_profile
        return render(request, 'candidate_profile.html', {'profile': profile})
    else:
        profile = request.user.employer_profile
        return render(request, 'employer_profile.html', {'profile': profile})



@login_required
def update_profile(request):
    if request.user.is_candidate:
        profile = get_object_or_404(CandidateProfile, user=request.user)
        form_class = CandidateProfileForm
        template_name = 'candidate_update_profile.html'  # Template for candidates
    elif request.user.is_employer:
        profile = get_object_or_404(EmployerProfile, user=request.user)
        form_class = EmployerProfileForm
        template_name = 'employer_update_profile.html'  # Template for employers
    else:
        raise Http404("Profile not found")

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Adjust this as necessary
    else:
        form = form_class(instance=profile)

    return render(request, template_name, {'form': form})



def candidate_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.user.save()
            user.is_candidate = True
            user.save()
            auth_login(request, user)
            CandidateProfile.objects.get_or_create(user=user)
            return redirect('Job_list')  # Redirect to candidate dashboard
    else:
        form = UserSignUpForm()
    return render(request, 'candidate_signup.html', {'form': form})

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_employer = True
            user.save()
            auth_login(request, user)
            EmployerProfile.objects.get_or_create(user=user)
            return redirect('job_list')  # Redirect to employer dashboard
    else:
        form = EmployerSignUpForm()
    return render(request, 'employer_signup.html', {'form': form})

def candidate_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_candidate:
                auth_login(request, user)
                CandidateProfile.objects.get_or_create(user=user)
                return redirect('job_list')  # Redirect to candidate dashboard
    else:
        form = UserLoginForm()
    return render(request, 'candidate_login.html', {'form': form})

def employer_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"Authenticated User: {user.username}")
                if user.is_employer:
                    auth_login(request, user)
                    EmployerProfile.objects.get_or_create(user=user)
                    return redirect('job_list')
                else:
                    print("User is not an employer.")
            else:
                print("User authentication failed.")
    else:
        form = UserLoginForm()
    return render(request, 'employer_login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('job_list') 