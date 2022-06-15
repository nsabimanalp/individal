from django.shortcuts import render
from myapp.models import Project


# Create your views here.
def index(request):
    work = Project.objects.all
    wk = {'work':work} 
    return render(request,'index.html', wk)

def details(request):
    # work = Project.objects.get(pk)
     return render(request,'details.html')