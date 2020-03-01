from django.contrib import admin

from .models import Category, Product, MenuItem, AddedItem, Cart, History, ExtraSelection
#from .models import Topping #, Sub, Extra, Primo, Platter, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(MenuItem)
admin.site.register(AddedItem)
admin.site.register(Cart)
admin.site.register(History)
admin.site.register(ExtraSelection)
#admin.site.register(Pizza)
#admin.site.register(Topping)
#admin.site.register(Sub)
#admin.site.register(Extra)
#admin.site.register(Primo)
#admin.site.register(Platter)
#admin.site.register(Cart)