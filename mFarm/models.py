import datetime
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Sacco(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(region="KE", null=True, blank=True)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_superuser(self, name, email, phone, password):
        user = self.model(email=self.normalize_email(email))
        user.phone = phone
        user.name = name
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

    def create_user(self, name, email, phone, password, sacco, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not sacco and not extra_fields.get('is_superuser'):
            raise ValueError('The sacco field must be set')
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            phone=phone,
            sacco=sacco,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Farmer(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    sacco = models.ForeignKey(Sacco, on_delete=models.CASCADE, null=True)
    phone = PhoneNumberField(region="KE")
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "name"]
    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.sacco = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MilkStatus(models.Model):
    FRESH = "fresh"
    SPOILT = "spoilt"
    MILK_STATUS_CHOICES = [
        (FRESH, 'Fresh'),
        (SPOILT, 'Spoilt'),

    ]

    status = models.CharField(
        max_length=7,
        choices=MILK_STATUS_CHOICES,
        default=FRESH
    )

    # spoilt = models.BooleanField(default=False)

    def __str__(self):
        return self.status


class Milk(models.Model):
    status = models.ForeignKey(MilkStatus, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    dateCollected = models.DateTimeField(auto_created=True, auto_now_add=True)

    # price

    def __str__(self):
        return "{} litres of {} milk from {}".format(self.quantity, self.status, self.farmer)


class MilkEvaluation(models.Model):
    the_milk = models.ForeignKey(Milk, on_delete=models.CASCADE)
    butter_fat = models.FloatField()
    # protein measured in g/100ml
    protein_content = models.FloatField()
    somevariable =0

    def calculate_base_amount(self):
        if self.the_milk.status.status == "fresh":
            butter_fat = 20.0
            protein = 50.0
            quantity = 100.0
            amount_total = (butter_fat * self.butter_fat) + (protein * self.protein_content) + (
                    quantity * self.the_milk.quantity)
            return amount_total
        else:
            return 0.0

    def __str__(self):
        return "{} Milk Evaluation".format(self.the_milk.farmer)


class MilkCollection(models.Model):
    dateCollected = models.DateTimeField(auto_now_add=True)
    evaluation = models.ForeignKey(MilkEvaluation, on_delete=models.CASCADE)
    farmerCollected = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return "Milk Collection from {}".format(self.farmerCollected.name)


class Billing(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    payment_period = models.DateField()
    amount = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):
        return "{} Billing Information".format(self.farmer.name)
