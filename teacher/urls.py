from django.urls import path
from . import views
urlpatterns = [
    path('assignmentreport/', views.assignmentreport, name='assignmentreport'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('assignmentcreator/', views.assignmentcreator, name='assignmentcreator'),
    path('docuploader/', views.docUploader, name='docUploader'),
]