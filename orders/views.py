from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pizza, Topping, Sub, Extra, Primo, Platter
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, "orders/index.html", {"message": None})


def menu(request):
    pizzas = Pizza.objects.all()
    imgurl = "/static/orders/images/"
    img = []
    for i in range(22, 32, 2):
        img.append(imgurl + "pizza/" + str(i) + ".jpg")

    if request.method == "POST":
        canOrder = request.user.is_authenticated
        debug = request.POST["addpizza"]
        # img = "/static/orders/images/pizza/0.jpg"
        context = {
            "user": request.user,
            "canOrder": canOrder,
            "pizzas": Pizza.objects.all(),
            "toppings": Topping.objects.all(),
            "subs": Sub.objects.all(),
            "extras": Extra.objects.all(),
            "primos": Primo.objects.all(),
            "platters": Platter.objects.all(),
            "cart": 1,
            "debug": debug,
            "img": img
        }
        return render(request, "orders/home.html", context)
    elif request.method == "GET":
        canOrder = request.user.is_authenticated
        # img = "/static/orders/images/pizza/0.jpg"        
        context = {
            "user": request.user,
            "canOrder": canOrder,
            "pizzas": Pizza.objects.all(),
            "toppings": Topping.objects.all(),
            "subs": Sub.objects.all(),
            "extras": Extra.objects.all(),
            "primos": Primo.objects.all(),
            "platters": Platter.objects.all(),
            "img": img
        }
        return render(request, "orders/home.html", context)

def login_view(request):
    if request.method == "GET":
        return render(request, "orders/login.html", {"message": None})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid Credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, "orders/register_success.html", {"message": None})
    else:
        form = RegistrationForm()
    return render(request, "orders/register.html", {"form": form})