from django.db import models

SIZE_CHOICES = (("S", "Small"), ("L", "Large"))

# Create your models here.
class Topping(models.Model): 
    TOPPING_CHOICES = (
                        ("PEPPERONI", "Pepperoni"),
                        ("SAUSAGE", "Sausage"),
                        ("MUSHROOMS", "Mushrooms"),
                        ("ONIONS", "Onions"),
                        ("HAM", "Ham"),
                        ("CANADIAN HAM", "Canadian Ham"),
                        ("PINEAPPLE", "Pineapple"),
                        ("EGGPLANT", "Eggplant"),
                        ("TOMATO AND BASIL", "Tomato & Basil"),
                        ("GREEN PEPPERS", "Green Peppers"),
                        ("HAMBURGER", "Hamburger"),
                        ("SPINACH", "Spinach"),
                        ("ARTICHOKE", "Artichoke"),
                        ("BUFFALO CHICKEN", "Buffalo Chicken"),
                        ("BARBECUE CHICKEN", "Barbecue Chicken"),
                        ("ANCHOVIES", "Anchovies"),
                        ("BLACK OLIVES", "Black Olives"),
                        ("FRESH GARLIC", "Fresh Garlic"),
                        ("ZUCCHINI", "Zucchini")
    )

    topping = models.CharField(max_length=64, choices=TOPPING_CHOICES)


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
    EXTRA_CHOICES = (
        ("Mushrooms", "+ Mushrooms"),
        ("Green Peppers", "+ Green Peppers"),
        ("Onions", "+ Onions")
    )

    extra = models.CharField(max_length=64, choices=EXTRA_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.get_extra_display()} for ${self.price}"

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

    def __str__(self):
        return f"{self.id}"