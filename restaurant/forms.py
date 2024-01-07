from django import forms
from django.utils import timezone


class BookingForm(forms.Form):
    name = forms.CharField(max_length=255)
    number_of_guest = forms.IntegerField(initial=6)
    bookings_date = forms.DateField(initial=timezone.now().date())
