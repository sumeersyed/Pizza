from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here

# Menu
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
            price = ""
        else:
            cat = ""
            if self.price:
                price = " (+$" + str(self.price) + ")"
            else:
                price = ""
        if self.size:
            size = self.get_size_display()
        else:
            size = ""
        if self.product.category.category_type == 'primary':            
            if self.product.stylized_name:
                return f"{size} {cat} {self.product.stylized_name}{price}"
            return f"{size} {cat} {self.product.name}{price}"
        else:
            if self.product.category == "Topping":
                return f"{cat} {self.product.name}"
            else:
                if self.product.stylized_name:
                    return f"{cat} {self.product.stylized_name}"
                else:
                    return f"{cat} {self.product.name}"

# Cart 
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField("MenuItem", through="AddedItem")
    ordered = models.BooleanField(default=False)
    ordered_time = models.DateTimeField(auto_now=False, null=True)
    delivered_time = models.DateTimeField(auto_now=False, null=True, blank=True)

    def totalquantity(self):
        q = 0
        for item in self.items.all():
            if item.product.category.category_type == 'primary':
                q += item.added_item.last().quantity
        return q

    def subtotal(self):
        total = 0
        for item in self.items.all():
            total += item.added_item.first().totalprice()
        return total

    def cartnumber(self):
        return 10000 + self.id

    """ def __str__(self):
        items = self.items.all()
        main = str(items[0])
        extras = "(" + ", ".join(str(x) for x in items[1:]) + ")" if items[1:] else ""
        return main + extras

    def total_sum(self):
        return sum(filter(None, [item.price for item in self.items.all()])) """

class AddedItem(models.Model):
    item = models.ForeignKey("MenuItem", on_delete=models.CASCADE, related_name="added_item")
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def totalprice(self):
        if self.extras.all():
            extrasprice = 0
            for extra in self.extras.all():
                for i in extra.item.all():
                    extrasprice += i.price
            return self.quantity * self.item.price + extrasprice
        else:
            return self.quantity * self.item.price

    def __str__(self):
        if self.extras.all():
            return f"{self.quantity} x {self.item} at ${self.item.price} = ${self.totalprice()}"
        else:
            return f"{self.quantity} x {self.item} at ${self.item.price} = ${self.totalprice()}"

    """def __str__(self):
        if self.extras.all():
            extras = self.extras.all()
            extrasprice = 0
            for extra in extras:
                extrasprice += extra.price  
            string = ", ".join(str(extra) for extra in extras)
            totalprice = self.item.price + extrasprice
            sentence = f"{self.quantity} x {self.item} with {self.item.product.addon_category}: " + string + f" at $" + str(totalprice)
            return sentence
        else:
            return f"{self.quantity} x {self.item.product.name} at ${self.item.price} = ${self.totalprice()}"
        #sentence = "{self.quantity} x {self.item.product.name} with {self.item.product.addon_category}: " + addons + " at {self.item.price} = {self.totalprice()}"
        # return f"{self.quantity} * {self.item.product.name} at {self.item.price} = {self.totalprice()}  """

class ExtraSelection(models.Model):
    item = models.ManyToManyField("MenuItem")
    main = models.ForeignKey("AddedItem", on_delete=models.CASCADE, related_name="extras")

    def __str__(self):
        if self.item:
            sentence = ", ".join(str(i) for i in self.item.all())
            return sentence
        else:
            return f"{self.item}"

class History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carts = models.ManyToManyField("Cart")