from rest_framework import serializers

from restaurant.models import Menu, Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['name', 'number_of_guest', 'bookings_date']


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        read_only = ['id']
