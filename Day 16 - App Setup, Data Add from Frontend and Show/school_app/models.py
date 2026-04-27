from django.db import models

# Create your models here.

class studentModel(models.Model):
  name = models.CharField(max_length=200)
  address = models.TextField()
  email = models.EmailField()
  admission_date = models.DateField()
  
  def __str__(self):
    return f'{self.name}'
