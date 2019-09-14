from django.db import models
from django.contrib.auth.models import User
class Quiz(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz_name=models.CharField(max_length=400)
    no_q=models.IntegerField(default=0)
    genre=models.CharField(max_length=400)
    count=models.IntegerField(default=1)
    array=models.IntegerField(default=0)
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=800)



class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=800)
class Player(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    name=models.CharField(max_length=400)

