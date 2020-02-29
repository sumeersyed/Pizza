from orders import models

SIZES = ("s", "l")

CATEGORIES = [
    # ("Regular Pizza", "primary"),
    # ("Sicilian Pizza", "primary"),
    # ("Sub", "primary"), 
    ("Pasta", "primary"),
    ("Salad", "primary"),
    ("Platter", "primary"),
    ("Topping", "topping"),
    ("Extra", "extra")
]

#for pair in CATEGORIES:
#    item = models.Category(name=pair[0], categorytype=pair[1])
#    item.save()


REGULAR_PIZZAS = [
    ("Cheese", 11.70, 16.45, 0),
    ("1 topping", 12.70, 18.45, 1),
    ("2 toppings", 14.20, 20.45, 2),
    ("3 toppings", 15.20, 22.45, 3),
    ("Special", 16.75, 24.45, 4)
]

SICILIAN_PIZZAS = [
    ("Cheese", 22.45, 35.70, 0),
    ("1 item", 24.45, 37.70, 1),
    ("2 items", 26.45, 39.70, 2),
    ("3 items", 27.45, 41.70, 3),
    ("Special", 28.45, 42.70, 4)
]

for data, cat_name in [(REGULAR_PIZZAS, "Regular Pizza"), (SICILIAN_PIZZAS, "Sicilian Pizza")]:
    cat = models.Category.objects.get(name=cat_name)
    addon_category = models.Category.objects.get(name="Toppings")
    for r in data:
        product = models.Product(name=r[0], category=cat, addon_category=addon_category, addon_limit=r[3])
        product.save()