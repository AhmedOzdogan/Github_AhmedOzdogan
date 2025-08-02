from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField() 
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"Booking {self.id} for {self.name} on {self.booking_date.strftime('%Y-%m-%d %H:%M:%S')}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - ${self.price} (Inventory: {self.inventory})"

