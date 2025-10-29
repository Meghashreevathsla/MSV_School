from django.shortcuts import render
from .models import allStudet
from .forms import StudentRegistration
# Create your views here.

def get_all(request):
    students = allStudet.objects.all()
    return render(request, 'register/egister.html', {'students':students, 'school_name': 'MSV_SCHOOL'})    

def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'register/formregistration.html',{'form':fm})