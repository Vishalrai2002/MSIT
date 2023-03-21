from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def certificateUpload(request, id):
    return render(request, 'student/studentCertificate.html')

def login(request):
    return render(request, 'student/studentLogin.html')

def signUp(request):
    return render(request, 'student/studentSignUp.html')

def profile(request, id):
    return render(request, f'student/{id}Profile.html')

def feedback(request, id):
    return render(request, 'student/studentFeedback.html')  
    
def assign(request):
    return render(request, 'student/quizstart.html') 

def assign1(request):
    return render(request, 'student/studentAssign.html')   
