from django.db import models


# Create your models here.
class Sacco(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=50)
    sacco = models.ForeignKey(Sacco, on_delete=models.SET_NULL(), null=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
