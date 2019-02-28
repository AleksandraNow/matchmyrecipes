from django.db import  models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE,)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE,)


class Post(models.Model):
    title =models.CharField(max_length=30, unique=True) 
    ingredients=models.TextField(max_length=290)
    description=models.TextField(max_length=10000)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE,)
    def __str__(self):
        return self.title


    
  
  
    
    
