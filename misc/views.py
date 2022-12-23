from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'misc/homePage.html')

def courses(request):       
    return render(request, 'misc/courses.html')

def feed(request):
    return render(request, 'misc/feed.html')

def leaderacad(request):
    return render(request, 'misc/leaderboardAcademics.html')

def leadercocurr(request):
    return render(request, 'misc/leaderboardCocurricular.html')

def contactUs(request): 
    return render(request, 'misc/contactUs.html')



