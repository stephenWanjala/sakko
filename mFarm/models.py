from string import Template as tm

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Sacco(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    # TODO("email & phone validation")

    def __str__(self):
        return self.name


class Farmer(models.Model):
    # TODO("farmer to be user)
    name = models.CharField(max_length=50)
    sacco = models.ForeignKey(Sacco, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)

    # TODO("email & phone validation)
    def __str__(self):
        return self.name


class MilkStatus(models.Model):
    fresh = models.BooleanField(default=True)
    spoilt = models.BooleanField(default=False)

    def __str__(self):
        if self.fresh:
            return "Fresh"
        else:
            "Spoilt"


class Milk(models.Model):
    status = models.ForeignKey(MilkStatus, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # date = models.DateField()
    # price

    def __str__(self):
        return tm('$farmer -> $status').substitute(farmer=self.farmer, quantity=self.status)


# class MilkCollection(models.Model):
#     dateCollected = models.DateTimeField(auto_now_add=True)
#     # quantityCollected
