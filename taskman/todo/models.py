from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=50)
    deadline = models.DateField(null=True,blank=True)
    created_on = models.DateField(auto_now = True)
    complete = models.BooleanField(default = False)
    status =models.BooleanField(default = False)

    def __str__(self):
        return self.task


    
