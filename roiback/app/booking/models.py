from django.db import models


class Hotel(models.Model):
    id = models.CharField(max_length=300, primary_key=True, unique=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.id


class Room(models.Model):
    id = models.CharField(max_length=300, primary_key=True, unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.RESTRICT, related_name='rooms')

    def __str__(self):
        return self.id


class Rate(models.Model):
    id = models.CharField(max_length=300, primary_key=True, unique=True)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT, related_name='rates')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.id


class Inventory(models.Model):
    id = models.CharField(max_length=300, primary_key=True, unique=True)
    rate = models.ForeignKey(Rate, on_delete=models.RESTRICT, related_name='breakdown')
    date = models.DateField()

    def __str__(self):
        return self.id
