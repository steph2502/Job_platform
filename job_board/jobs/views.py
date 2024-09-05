
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from .forms import JobForm, ApplicationForm
from accounts.models import CandidateProfile

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    requirements = job.get_requirements_list()
    return render(request, 'job_detail.html', {'job': job,'requirements': requirements})

@login_required
def job_create(request):
    if request.user.is_employer: 
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():
                job = form.save(commit=False)
                job.employer = request.user.employer_profile 
                job.save()
                return redirect('job_list')
        else:
            form = JobForm()
        return render(request, 'job_create.html', {'form': form})
    else:
        return redirect('job_list') 


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    try:
        candidate_profile = CandidateProfile.objects.get(user=request.user)
    except CandidateProfile.DoesNotExist:
        pass
        return redirect('job_list')

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                candidate_profile = CandidateProfile.objects.get(user=request.user)
            except CandidateProfile.DoesNotExist:
                return redirect('job_list')
            application = form.save(commit=False)
            application.job = job
            application.candidate = candidate_profile  
            application.save()
            return redirect('application_tracking')  
    else:
        form = ApplicationForm()
    
    return render(request, 'apply_job.html', {'form': form, 'job': job})


@login_required
def application_tracking(request):
    if request.user.is_candidate:
        applications = Application.objects.filter(candidate__user=request.user)
        return render(request, 'track_application.html', {'applications': applications})
    else:
        return redirect('job_list') 