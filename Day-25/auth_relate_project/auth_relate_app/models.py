from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
  full_name=models.CharField(max_length=100,null=True)
  
  def __str__(self):
    return f'{self.username}'
 
class ProfileModel(models.Model):
  user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='user_profile',null=True)
  address = models.TextField(null=True)
  dob = models.DateField(null=True)
  image = models.ImageField(upload_to='profile_img', null=True)
  
  def __str__(self):
    return f'{self.user.username}'
                              
class ProductModel(models.Model):
  name = models.CharField(max_length=200, null=True)
  description = models.TextField(null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
  qty = models.PositiveIntegerField(null=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
  created_by = models.ForeignKey(null=True)
  
  