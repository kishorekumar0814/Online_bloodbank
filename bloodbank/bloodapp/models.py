from django.db import models


# Create your models here.
class signin(models.Model):
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

    def __str__(self):
        return self.username


class register(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    confirm_password = models.CharField(max_length=225)
    email_id = models.CharField(max_length=225)
    ph_no = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
    blood_group = models.CharField(max_length=225)

    def __str__(self):
        return self.firstname


class blooddata(models.Model):
    blood_group = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    age = models.CharField(max_length=225)
    ph_no = models.CharField(max_length=225)
    place = models.CharField(max_length=225)

    def __str__(self):
        return self.blood_group



# Create your models here.
