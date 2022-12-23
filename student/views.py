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
    return render(request, 'student/studentProfile.html')

# def feedbackCalculator(id):

    
def feedback(request, id):
    return render(request, 'student/studentFeedback.html')  
