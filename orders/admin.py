from django.contrib import admin

from .models import Pizza, Topping, Sub, Extra, Primo, Platter, Cart

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(Primo)
admin.site.register(Platter)
admin.site.register(Cart)