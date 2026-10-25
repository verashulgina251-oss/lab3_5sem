from django.test import TestCase
from django.utils import timezone
from .models import Order, OrderStatus, Dispatcher

class TaxiOrderModelTests(TestCase):
    def test_order_creation(self):
        status = OrderStatus.objects.create(status_code=1, status_name="Новый")
        dispatcher = Dispatcher.objects.create(
            dispatcher_code=1,
            last_name="Иванов",
            first_name="Иван",
            middle_name="Иванович",
            birth_date="1990-01-01",
            passport_data="1234 567890",
            phone="+79990000000"
        )
        
        order = Order.objects.create(
            order_code=1,
            incoming_datetime=timezone.now(),
            assignment_datetime=timezone.now(),
            departure_place="Центр",
            destination_place="Вокзал",
            client_phone="+79001112233",
            cost=750.00,
            status=status,
            dispatcher=dispatcher
        )
        
        self.assertEqual(order.cost, 750.00)
        self.assertEqual(str(status), "Новый")