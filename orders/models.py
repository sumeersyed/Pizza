from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Category(models.Model):
    CATEGORY_TYPES = (("primary", "Primary"), ("topping", "Topping"), ("extra", "Extra"))
    name = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=64, blank=True, null=True)
    category_type = models.CharField(max_length=16, choices=CATEGORY_TYPES, default="primary")

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=64)
    stylized_name = models.CharField(max_length=64, null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    addon_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="related_products", blank=True, null=True)
    addon_limit = models.IntegerField(default=0, null=True)

    def __str__(self):
        if self.stylized_name:
            return f"{self.stylized_name} {self.category}"
        else:
            return f"{self.name} {self.category}"

class MenuItem(models.Model):
    SIZE_CHOICES = (("s", "Small"), ("l", "Large"))
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="menu_items")
    size = models.CharField(max_length=16, choices=SIZE_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        if self.product.category.category_type == 'primary':
            cat = self.product.category.name + " - "
        else:
            cat = ""
        if self.size:
            size = self.get_size_display()
        else:
            size = ""
        if self.price:
            price = ": $" + str(self.price)
        else:
            price = ""
        return f"{size} {cat} {self.product.name} {price}"