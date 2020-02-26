from django.db import models
from django.contrib.auth.models import User

SIZE_CHOICES = (("S", "Small"), ("L", "Large"))

# Create your models here.
class Topping(models.Model): 
    topping = models.CharField(max_length=64)
    toppingStylized = models.CharField(max_length=64, default="NOT NULL")
    promotional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.toppingStylized}"


class Pizza(models.Model):
    
    PIZZA_TYPE = (("sicilian", "Sicilian"), ("regular", "Regular"))
    PIZZA_TOPPINGS = ((0, "Cheese"), (1, "1 Topping"), (2, "2 Toppings"), (3, "3 Toppings"), (4, "Special Toppings"))

    pizzaType = models.CharField(max_length=32, choices=PIZZA_TYPE)
    sPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    lPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    numberoftoppings = models.IntegerField(choices=PIZZA_TOPPINGS, default=0)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f"{self.get_pizzaType_display()} Pizza with {self.get_numberoftoppings_display()}: ${self.sPrice} (S), ${self.lPrice} (L)"

class Extra(models.Model):

    extra = models.CharField(max_length=64)
    extraStylized = models.CharField(max_length=64, default="NOT NULL")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    promotional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.extraStylized} for ${self.price}"

class Sub(models.Model):

    subName = models.CharField(max_length=64)
    sPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    lPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    addextra = models.CharField(max_length=64, null=True)
    extras = models.ManyToManyField(Extra, blank=True)
    extraCheese = models.BooleanField(default=False)

    def __str__(self):
        if self.extraCheese:
            return f"{self.subName} with Extra Cheese: ${self.sPrice + 0.50} (S), ${self.lPrice + 0.50} (L)"
        else:
            return f"{self.subName}: ${self.sPrice} (S), ${self.lPrice} (L)"

class Primo(models.Model):

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}: ${self.price}"

class Platter(models.Model):

    name = models.CharField(max_length=64)
    sPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    lPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}: ${self.sPrice} (S), ${self.lPrice} (L)"

class Cart(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
    subs = models.ManyToManyField(Sub, blank=True)
    platters = models.ManyToManyField(Platter, blank=True)
    primos = models.ManyToManyField(Primo, blank=True)

    def order(self):
        orders = ""
        for pizza in self.pizzas.all():
            orders += pizza.__str__()
        return orders

    def __str__(self):
        return f"{self.id}: {self.pizzas}"