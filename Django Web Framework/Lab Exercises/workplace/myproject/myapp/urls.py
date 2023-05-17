from django.urls import path
from . import views

urlpatterns = [
    # from week 2 - views lab exercise
    # path("", views.home, name="home"),

    # from week 2 - requests and urls lab exercise
    # path("drinks/<str:drink_name>", views.drinks, name="drink_name"),

    # from week 2 - creating urls and views and urls lab exercise
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),

    # from week 3 - working with forms lab exercise
    path("booking/", views.booking, name="booking"),

]
