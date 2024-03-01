from django import forms 
  
class ApplicantForm(forms.Form): 
    first_name = forms.CharField()
    last_name = forms.CharField()
    resume_field = forms.FileField() 