from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Menu


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
# def home(request):
#     return HttpResponse("Welcome to Little Lemon!")


# def about(request):
#     return HttpResponse("About Us")


# def menu(request):
#     return HttpResponse("Menu")


# from week 3 - working with forms lab exercise
def booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


# from week 4 - creating dynamic templates lab exercise
# def menu(request):
#     return render(request, 'menu.html')


# def about(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional "
#                               "recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, "
#                               "and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The "
#                               "restaurant has a rustic and relaxed atmosphere with moderate prices, making it a "
#                               "popular place for a meal any time of the day."}

#     return render(request, 'about.html', {'content': about_content})


# from week 4 - creating dynamic templates lab exercise
# def menu(request):
#     menu_items = Menu.objects.all()
#     items_dict = {'menu': menu_items}
#     return render(request, 'menu.html', items_dict)


# from week 4 - working with templates lab exercise
def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    return render(request, 'book.html')
