from django import forms
from django.db import models


# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=80)
    confirm_password = models.CharField(max_length=90)

    def str(self):
        return self.username

class District(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    wikipedia_link = models.URLField()

    def str(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name
class UserInfo(models.Model):

        name = models.CharField(max_length=100)
        dob = models.DateField()
        age = models.IntegerField()
        gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
        phone_number = models.CharField(max_length=10)
        email_id = models.EmailField()
        address = models.TextField()
        district = models.ForeignKey(District, on_delete=models.CASCADE)  # Assuming District is another model
        branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Assuming Branch is another model
        account_type = models.ForeignKey(AccountType,choices=[('Saving Account', 'Saving Accoont'), ('Current Account', 'Current Account'), ('other', 'Other')], on_delete=models.CASCADE)  # Assuming AccountType is another model
        materials_provided = models.ManyToManyField(Material)



        def str(self):
            return self.name