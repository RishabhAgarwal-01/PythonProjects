from datetime import date, timedelta
from typing import List
from customer import Customer
from car import Car

class Reservation:
    def __init__(self,reservation_id, customer:Customer, car:Car, start_date:date, end_date:date):
        self.reservation_id = reservation_id
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_total_cost()
    
    def calculate_total_cost(self):
        return (self.end_date - self.start_date).days * self.car.get_rental_price_per_day
    
    @property
    def get_start_date(self):
        return self.start_date
    
    @property
    def get_end_date(self):
        return self.end_date
    
    @property
    def get_car(self):
        return self.car
    
    @property
    def get_total_price(self):
        return self.total_cost
    
    @property
    def get_reservation(self):
        return self.reservation_id

