# Project 3: Pizza
---
### Web Programming with Python and JavaScript
#### Note: bolded points are works in progress

---
## App-in-Action
https://www.youtube.com/watch?v=_a83t6Bb-Uk

---
## Overview
(full requirements: [here](https://docs.cs50.net/ocw/web/projects/3/project3.html))
Project 3 gets us to use Django, a Python-based free and open-source web framework to create a semi-complex, database-driven website, or a full-service Pizza website that handles:
1. User registration / login / logout
2. Full menu of a variety of different items stored in a database (Django's default -- SQLite)
3. Ability for site admins to add/update/remove items into  menu through Django Admin at URL localhost/admin
4. Shopping cart where user can view his added items and total price, etc
5. Ability to place order once at least one item is in the cart
6. Site admin can view orders placed through Django Admin) **(Cannot be explicitly seen in case of big data; decoupled it a little such that it works like this: History contains all the Carts (or orders) made by a particular user, and Carts contain all the items made in that particular Cart (order instance)**
7. Payment API (Iffy: Bootstrap template)
8. **Mobile-friendly**

## Technology Used:
1. Django
2. SQLite (in the form of Django Models)
3. HTTP (GET and POST requests)
4. **API (to implement payment)**

## Languages:
1. Python (backend: Django)
2. HTML (website templates)
3. CSS (HTML Styling)
4. Django templating language (parsing variables from Python views to HTML)
5. Django Models (database)
6. Bootstrap (styling HTML)
7. Javascript (not really, but implementing Google Maps snippet and topping choices dropdown)

### Images courtesy of friendly-neighbourhood **Google**, except for the image of the pizza on a plate which is used as the background image and for the menu, which was taken by me in Firenze, Italia

---
## To-do
1. Write a Python file that auto populates the databases, etc
2. Make the order history page better looking
3. Ability for site admin to look at order history (without going in a roundabout way)
4. Mobile-friendly
5. Payment API implementation
6. Deployment

## Reflection
Honestly, this project took quite some time, and it was rather fun. However, towards the end, it was a little draining, partly because of how complex the Model relationshipss (SQL tables) became. It got a little daunting to debug and even with Django's ability to retroactively update some tables, it was becoming harder. A big reason is that the Models and their relationships were not well established and designed from the start. Most of it were created to have a working webapp, and only after they were implemented, did I get a better idea on how to better design the Models and relationships.

Nesting in HTML also became pretty tedious due to the Models' relationships and the fact that Django's templating in HTML do not have built-in features in IDE naturally.

If possible and if time permits, I would revamp and rework the second part of the Models (the Cart part). I redid the Menu part of the Models 3 times, and by then, I just wanted to finish the project as it became quite taunting. I tried to keep everything to purely HTML and CSS on the client side as I wanted to see how far I can take it without JavaScript. JS, however, has to be used for small little parts which I did not actually touch much as they were templates/embeds. 

More or less, I feel a lot more comfortable with using Django and Git (which was also my personal focus for this project). I also feel like I have learned to better visualize and design Models and their relationships. (SQL data)

## Model Relationship
1. The menu.html displays MenuItems (which are extensions of Products, which are either 'primary', 'topping' or 'extra'
2. Product is the general class for an item product; thus a Large Cheese Regular Pizza and a Small Cheese Regular Pizza MenuItem belongs to the same product: a Regular Pizza, category "primary", with addon_category of "topping" and addon_limit of 0
3. The cart.html displays Cart, with a M2M relationship with MenuItemm through AddedItem
4. An AddedItem is basically an item selection that has been added into the cart -- it contains information on which cart, and how many of it
5. ExtraSelection accompanies AddedItems that are Pizzas or Subs with > 0 addon_limits, which are topping/extra selection that accompanies the AddedItem
6. Lastly, History references User as a FK, in order words, each user has their own History, which shows the carts that have been previously ordered by the person

---
## Setup
**To-do**

---
## Improvements/bugs
**To-do** 
