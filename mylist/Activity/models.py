from django.db import models


# Create your models here.
class r_data(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField()
    Adress=models.CharField(max_length=50,default="")
    Contact=models.IntegerField()
    Mail=models.CharField(max_length=50,default="")

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username
