from django.contrib import admin

from ordini.models import Order,OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)