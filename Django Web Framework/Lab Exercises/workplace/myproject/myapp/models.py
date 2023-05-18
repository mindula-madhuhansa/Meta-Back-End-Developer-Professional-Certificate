from django.db import models


# Create your models here.

# from week 3 - models and migrations lab exercise
# class Drinks(models.Model):
#     drink_name = models.CharField(max_length=200)
#     price = models.IntegerField()


# from week 3 - models using foreign keys lab exercise
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)


# from week 3 - working with forms lab exercise
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField(default=1)
    reservation_time = models.DateField(auto_now=True)
    comment = models.CharField(max_length=1000)


# from week 3 - using django admin lab exercise
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name
    