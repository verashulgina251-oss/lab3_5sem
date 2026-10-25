from django.contrib import admin
from .models import Driver, Car, OrderStatus, Dispatcher, Order

class CarInline(admin.TabularInline):
    model = Car
    extra = 1

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'license_number')
    search_fields = ('last_name', 'license_number')
    inlines = [CarInline]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'brand', 'color', 'driver')
    list_filter = ('brand', 'color')
    search_fields = ('car_number', 'brand')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'departure_place', 'destination_place', 'cost', 'status', 'dispatcher')
    list_filter = ('status', 'incoming_datetime')
    search_fields = ('client_phone', 'departure_place', 'destination_place')

admin.site.register(OrderStatus)
admin.site.register(Dispatcher)