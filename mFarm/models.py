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

    # date = models.DateField()
    # price

    def __str__(self):
        return "{} litres of {} milk from {}".format(self.quantity, self.status, self.farmer)


class MilkEvaluation(models.Model):
    the_milk = models.ForeignKey(Milk, on_delete=models.CASCADE)
    butter_fat = models.FloatField()
    # protein measured in g/100ml
    protein_content = models.FloatField()
    quantity_supplied = models.FloatField()
    gross_price = models.FloatField()

    def calculate_base_amount(self):
        butter_fat = 20.0
        protein = 50.0
        quantity = 100.0
        amount_total = (butter_fat * self.butter_fat) + (protein * self.protein_content) + (
                quantity * self.quantity_supplied)
        return amount_total

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
