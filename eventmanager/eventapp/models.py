from django.db import models

# Create your models here.

class participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class program(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    speaker = models.ForeignKey(participant,on_delete=models.CASCADE,max_length=100)
    topic = models.CharField(max_length=200)
    
    def __str__(self):
        return self.day
    
