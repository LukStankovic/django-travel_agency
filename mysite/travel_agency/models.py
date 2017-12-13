from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthdate = models.DateField('birthdate')
    people = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.surname

class Destination(models.Model):
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Excursion(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    datetime = models.DateTimeField('excursion date')
    desc = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.desc

