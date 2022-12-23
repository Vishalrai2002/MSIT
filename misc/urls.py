from django.urls import path
from . import views
urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('linkyfeed/', views.feed, name='feed'),
    path('', views.home, name='home'),
    path('leaderboard/academics/', views.leaderacad, name='leaderacad'),
    path('leaderboard/cocurricular/', views.leadercocurr, name='leadercocurr'),
    path('contactUs/', views.contactUs, name='contactUs'),

]