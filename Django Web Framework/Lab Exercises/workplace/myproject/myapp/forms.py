from django import forms
from .models import Booking


# from week 3 - working with forms lab exercise
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
