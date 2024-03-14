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

def test(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST, request.FILES)
        # if form.is_valid():
            # resume_field = form.cleaned_data['resume_field']
            
            # for f in resume_field:
                # entry = Applicants(resume=f)
                # entry.save()
            
            # return render(request, "thankyou.html")
    context = {} 
    context['form'] = ApplicantForm() 
    return render( request, "home.html", context)


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
    if request.method == "POST":
        form = ApplicantForm(request.POST,request.FILES)
        if form.is_valid():
            resume_field = form.cleaned_data['resume_field']
            data = {}
            data["results"] = []
            for f in resume_field:
                entry = Applicants(resume=f)
                entry.save()
                
            all_resumes = Applicants.objects.all()
            for i in all_resumes:
                resume_text = clean_string(extract_text_from_pdf("resume_screener/media/"+str(i.resume)))
                job_desc_text = """
                                Java Documentation XML BPM User Interface Design Deployment Business Process Troubleshooting SOAP SQL Analysis JavaScript Database SDLC Business Analyst HTML Data Modeling Collaboration Mentoring Communication Skills Technical Computer Science Software Development
                                """
                data["results"].append({"res_name":str(i.resume),"overall":compare_resume(resume_text,job_desc_text)})
            return render(request, "candidates.html", data)
    context = {} 
    context['form'] = ApplicantForm() 
    return render(request, "candidates-e.html", context) 
    
def candidates(request):
    # if request.method == "POST":
        # form = ApplicantForm(request.POST)
        # if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # resume_field = form.cleaned_data['resume_field']
            
            
            # return render(request, "thankyou.html")
            
    return render(request, "candidates.html")
    
    
import PyPDF2
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
#PyPDF2.__version__

def extract_text_from_pdf(pdf_path):
  with open(pdf_path,"rb") as f:
      reader = PdfReader(f)
      results = []
      for i in range(0,len(reader.pages)):
          selected_page = reader.pages[i]
          text = selected_page.extract_text()
          results.append(text)
      return '/n'.join(results)

def clean_string(text):
  bad_chars = ['$', '#', '^', "*", "?", "[", "]", "{", "}", "+", "=", '_', "<", ">", "/", "|", "~", "!", "•", "-", "(", ")", "’", "@"]
  clean_text = text.replace("\n"," ")
  clean_text = ''.join(i for i in clean_text if not i in bad_chars)
  
  tokens = nltk.word_tokenize(clean_text)
  tagged = nltk.pos_tag(tokens)
  
  final_text = ""
  for x in tagged:
    if "N" == x[1][0] or "FW" == x[1]:
        final_text += x[0]
        final_text += " "
  return final_text

def compare_resume(resume,job_desc):
  compare = [job_desc,resume]
  matrix = CountVectorizer().fit_transform(compare)
  similarity_matrix = cosine_similarity(matrix)
  return "{:.2f}%".format(similarity_matrix[1][0]*100)