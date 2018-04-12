from django.db import models

# Create your models here.
class User(models.Model):
    #user_id = models.AutoField(primary_key=true)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_address = models.CharField(max_length=200)
    user_birthdate = models.DateField()
    user_password = models.CharField(max_length=50)
