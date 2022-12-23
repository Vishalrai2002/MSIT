from django.urls import path
from . import views
urlpatterns = [
    path('certificateUpload/<str:id>/', views.certificateUpload, name='certificateUpload'),
    path('login/', views.login, name='login'),
    path('signUp/', views.certificateUpload, name='certificateUpload'),
    path('profile/<str:id>/', views.certificateUpload, name='certificateUpload'),
    path('feedback/<str:id>/', views.feedback, name='feedback'),

]