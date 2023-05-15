from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# from week 2 - views lab exercise
# def home(request):
#     return HttpResponse("<h1>Welcome to Little Lemon!</h1>")


# from week 2 - requests and urls lab exercise
# def drinks(request, drink_name):
#     drink = {
#         "mocha": "type of coffee",
#         "tea": "type of beverage",
#         "lemonade": "type of refreshment"
#     }
#     choice_of_drink = drink[drink_name]
#     return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)


# from week 2 - creating urls and views and urls lab exercise
def home(request):
    return HttpResponse("Welcome to Little Lemon!")


def about(request):
    return HttpResponse("About Us")


def menu(request):
    return HttpResponse("Menu")


def book(request):
    return HttpResponse("Make a booking")
