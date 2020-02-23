from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    pub_data = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=32)