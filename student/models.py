from django.db import models
from django.utils.translation import autoreload_started
from django.contrib.auth.models import User

class studentProfile(models.Model):
    student_id= models.CharField(max_length=100)
    student_name= models.ForeignKey(User, on_delete=models.CASCADE)
    student_class= models.CharField(max_length=100)
    student_email= models.CharField(max_length=100)
    student_phone= models.IntegerField()
    student_address= models.CharField(max_length=100)
    id_created= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_id
    class Meta:
        ordering = ['id_created']


class studentPerformance(models.Model):
    academics= models.JSONField()
    cocurricular= models.JSONField()
    student_id= models.ForeignKey(studentProfile, on_delete=models.CASCADE)
    last_action= models.DateTimeField(auto_now_add=True)
    group= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    blood_group= models.CharField(max_length=100)

    def __str__(self):
        return self.student_id

class Linkify(models.Model):
    content= models.CharField(max_length=1000)
    student_id= models.CharField(max_length=100)
    student_name= models.ForeignKey(User, on_delete=models.CASCADE)
    post_created= models.DateTimeField(auto_now_add=True)
    likes= models.IntegerField()
    comments= models.IntegerField()
    def __str__(self):
        return self.student_id
    class Meta:
        ordering = ['post_created']
