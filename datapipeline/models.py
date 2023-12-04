from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=100)
    assigned_id = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Message(models.Model):
    session_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.student_id} in {self.session_id}"

class CustomGPT(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100, default='Sai')
    university = models.CharField(max_length=100, default='UCSC')
    gpt_type = models.CharField(max_length=50,default='')
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class FireData(models.Model):
    data = models.JSONField()