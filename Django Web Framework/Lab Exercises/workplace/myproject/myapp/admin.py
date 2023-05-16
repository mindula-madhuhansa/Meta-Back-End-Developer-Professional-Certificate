from django.contrib import admin
from .models import Drinks, DrinksCategory

# Register your models here.

# from week 3 - models and migrations lab exercise
# admin.site.register(Drinks)

# from week 3 - models using foreign keys lab exercise
admin.site.register(DrinksCategory)
admin.site.register(Drinks)
