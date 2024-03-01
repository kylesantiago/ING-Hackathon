from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicantForm
from .models import Applicants

def home(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            resume_field = form.cleaned_data['resume_field']

            entry = Applicants(first_name=first_name,last_name=last_name,resume=resume_field)
            entry.save()
            
            return render(request, "thankyou.html")
    context = {} 
    context['form'] = ApplicantForm() 
    return render( request, "home.html", context) 
