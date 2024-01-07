from django.test import Client
from restaurant.models import Booking, Menu

from random import randint


BOOKINGS = {
    1: {'name': 'Vill'},
    2: {'name': 'Jani', 'no_og_guests': randint(1, 11)},
    3: {'name': 'Niilo', 'no_og_guests': randint(1, 11)},
    4: {'name': 'Markus', 'no_og_guests': randint(1, 11)},
}

MENU_ITEMS = {
    1: {'title': 'ApplePie', 'price': 13.78},
    2: {'title': 'VanillaLatte', 'price': 3.99, 'inventory': randint(0, 11)},
    3: {'title': 'Icecream', 'price': 5.00, 'inventory': randint(0, 11)},
    4: {'title': 'IrishCoffe', 'price': 7.89, 'inventory': randint(0, 11)},
}


class UserMixin:

    def create_user(self, username, password):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {
            'username': username,
            'password': password,
        }
        return Client().post(url, data=data)

    def get_token(self, username, password):
        url = 'http://127.0.0.1:8000/api/token/login/'
        data = {
            'username': username,
            'password': password,
        }
        return Client().post(url, data=data).data.get('access')

    def get_auth_header(self, token):
        return {'Authorization': f'JWT {token}'}


class BookingMixin:
    bookings = BOOKINGS

    def create_bookings(self):
        for idx in self.bookings.keys():
            booking = Booking.objects.create(
                name=self.bookings[idx]['name'],
            )
            if self.bookings[idx].get('number_of_guest') is not None:
                booking.number_of_guest = self.bookings[idx]['number_of_guest'],
            if self.bookings[idx].get('bookings_date') is not None:
                print(self.bookings[idx]['bookings_date'])
                booking.bookings_date = self.bookings[idx]['bookings_date'],
            booking.save()


class SingleBookingMixin:
    booking = BOOKINGS.get(1)

    def create_booking(self):
        booking = Booking.objects.create(
            name=self.booking.get('name'),
        )
        if self.booking.get('number_of_guest') is not None:
            booking.number_of_guest = self.booking.get('number_of_guest')
        if self.booking.get('bookings_date') is not None:
            booking.bookings_date = self.booking.get('boooking_date')
        booking.save()
        self.booking = booking


class MenuItemMixin:
    items = MENU_ITEMS

    def create_menu_items(self):
        for idx in self.items.keys():
            item = Menu.objects.create(
                title=self.items[idx]['title'],
                price=self.items[idx]['price'],
            )
            if self.items[idx].get('inventory') is not None:
                item.inventory = self.items[idx].get('inventory')
            item.save()


class SingleMenuItemMixin:
    item = MENU_ITEMS.get(1)

    def create_menu_item(self):
        item = Menu.objects.create(
            title=self.item['title'],
            price=self.item['price'],
        )
        if self.item.get('inventory') is not None:
            item.inventory = self.item.get('inventory')
        item.save()
        self.menu_item = item
