from django.db import models

class Driver(models.Model):
    driver_code = models.IntegerField(primary_key=True, db_column='Код водителя')
    last_name = models.CharField(max_length=30, db_column='Фамилия')
    first_name = models.CharField(max_length=30, db_column='Имя')
    middle_name = models.CharField(max_length=30, db_column='Отчество')
    birth_date = models.DateField(db_column='Дата рождения')
    license_number = models.CharField(max_length=20, unique=True, db_column='Номер водительского удостоверения')
    passport_data = models.CharField(max_length=20, unique=True, db_column='Паспортные данные')
    phone = models.CharField(max_length=30, db_column='Телефон')

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.phone})"


class Car(models.Model):
    car_code = models.IntegerField(primary_key=True, db_column='Код автомобиля')
    car_number = models.CharField(max_length=10, db_column='Номер автомобиля')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, db_column='Код водителя')
    brand = models.CharField(max_length=30, db_column='Марка')
    color = models.CharField(max_length=30, db_column='Цвет')
    year = models.IntegerField(db_column='Год_выпуска')

    def __str__(self):
        return f"{self.brand} — {self.car_number}"


class OrderStatus(models.Model):
    status_code = models.IntegerField(primary_key=True, db_column='Код статуса')
    status_name = models.CharField(max_length=30, db_column='Статус')

    def __str__(self):
        return self.status_name


class Dispatcher(models.Model):
    dispatcher_code = models.IntegerField(primary_key=True, db_column='Код диспетчера')
    last_name = models.CharField(max_length=30, db_column='Фамилия')
    first_name = models.CharField(max_length=30, db_column='Имя')
    middle_name = models.CharField(max_length=30, db_column='Отчество')
    birth_date = models.DateField(db_column='Дата рождения')
    passport_data = models.CharField(max_length=20, unique=True, db_column='Паспортные данные')
    phone = models.CharField(max_length=30, db_column='Телефон')

    def __str__(self):
        return f"Диспетчер: {self.last_name} {self.first_name}"


class Order(models.Model):
    order_code = models.IntegerField(primary_key=True, db_column='Код заказа')
    incoming_datetime = models.DateTimeField(db_column='Дата и время поступления заказа')
    assignment_datetime = models.DateTimeField(db_column='Дата и время назначения')
    departure_place = models.CharField(max_length=100, db_column='Место отправления')
    destination_place = models.CharField(max_length=100, db_column='Место назначения')
    client_phone = models.CharField(max_length=30, db_column='Телефон клиента')
    cost = models.DecimalField(max_digits=10, decimal_places=2, db_column='Стоимость')
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, db_column='Код автомобиля')
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=1, db_column='Код статуса')
    dispatcher = models.ForeignKey(Dispatcher, on_delete=models.CASCADE, db_column='Код диспетчера')

    def __str__(self):
        return f"Заказ #{self.order_code} ({self.departure_place} -> {self.destination_place})"