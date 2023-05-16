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
