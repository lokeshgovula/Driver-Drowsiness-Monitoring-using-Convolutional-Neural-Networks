from django.db import models


# Create your models here.
class DriverRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    vehiclenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'DriversRegistrations'


# Create your models here.
class FattigueInfoModel(models.Model):
    user_name = models.CharField(max_length=100)
    login_user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    vehiclenumber = models.CharField(max_length=100)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    fatigue = models.CharField(max_length=100)
    c_date = models.DateField()
    def __str__(self):
        return self.login_user

    class Meta:
        db_table = 'FatigueInfo'
