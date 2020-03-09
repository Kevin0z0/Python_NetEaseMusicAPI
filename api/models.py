from django.db import models

# Create your models here.


class API(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Our Door", "Our Door")
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    categroy = models.CharField(max_length=200, null=True, choices=CATEGORY)
    discription = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Customer(models.Model):
    STATUS = (
        ("Peding", "Peding"),
        ("Out for delivery", "Out for delivery"),
        ("Delivered", "Delivered")
    )

    customer = models.CharField(max_length=200, null=True)
    product = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
