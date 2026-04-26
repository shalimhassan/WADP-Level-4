from django.db import models
from crud_app import *

# Create your models here.
class TeacherModel(models.Model):
  name = models.CharField(max_length=100,null=True)
  department = models.CharField(max_length=100,null=True)
  email = models.EmailField(null=True)
  
  def __str__(self):
    return f'{self.name} - {self.department}'
  