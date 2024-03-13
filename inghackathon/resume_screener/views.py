from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicantForm
from .models import Applicants

def home(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST, request.FILES)
        # if form.is_valid():
            # resume_field = form.cleaned_data['resume_field']
            
            # for f in resume_field:
                # entry = Applicants(resume=f)
                # entry.save()
            
            # return render(request, "thankyou.html")
    # context = {} 
    # context['form'] = ApplicantForm() 
    return render( request, "index.html") 


def newjob(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST)
        # if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # resume_field = form.cleaned_data['resume_field']
            
            
            # return render(request, "thankyou.html")
            
    return render(request, "new-job.html") 
    
def candidate(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST)
        # if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # resume_field = form.cleaned_data['resume_field']
            
            
            # return render(request, "thankyou.html")
            
    return render(request, "candidates-e.html") 
    
def candidates(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST)
        # if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # resume_field = form.cleaned_data['resume_field']
            
            
            # return render(request, "thankyou.html")
            
    return render(request, "candidates.html")