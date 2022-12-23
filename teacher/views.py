from django.shortcuts import render
from django.http import HttpResponse

def assignmentreport(request):
    return render(request, 'teacher/teacherAssignmentReport.html')

def login(request):
    return render(request, 'teacher/teacherLogin.html')

def signUp(request):
    return render(request, 'teacher/teacherSignUp.html')

def assignmentcreator(request):
    return render(request, 'teacher/teacherAssignmentcreator.html')

def docUploader(request):
    return render(request, 'teacher/teacherTask.html')





