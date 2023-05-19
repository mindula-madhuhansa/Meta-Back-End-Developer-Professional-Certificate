from django.contrib import admin
from .models import Drink
from .models import DrinksCategory
from .models import Booking
from .models import Employee
from .models import Menu


# Register your models here.

# from week 3 - models and migrations lab exercise
# admin.site.register(Drinks)

# from week 3 - models using foreign keys lab exercise
admin.site.register(DrinksCategory)
admin.site.register(Drink)

# from week 3 - working with forms lab exercise
admin.site.register(Booking)

# from week 3 - using django admin lab exercise
admin.site.register(Employee)

# from week 4 - creating dynamic templates lab exercise
admin.site.register(Menu)
