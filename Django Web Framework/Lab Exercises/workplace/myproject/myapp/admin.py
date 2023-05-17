from django.contrib import admin
from .models import Drinks
from .models import DrinksCategory
from .models import Booking


# Register your models here.

# from week 3 - models and migrations lab exercise
# admin.site.register(Drinks)

# from week 3 - models using foreign keys lab exercise
admin.site.register(DrinksCategory)
admin.site.register(Drinks)

# from week 3 - working with forms lab exercise
admin.site.register(Booking)
