import uuid
from credit_card_payment_processor import CreditCardPaymentProcessor
from paypal_payment_processor import PayPalPaymentProcessor
from reservation import Reservation
from customer import Customer
from car import Car

class RentalSystem:
    _instance = None
    def __init__(self):
        if RentalSystem._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RentalSystem._instance = self
            self.reservations = {}
            self.cars= {}
            self.payment_processors = {
                'credit_card': CreditCardPaymentProcessor(),
                'paypal': PayPalPaymentProcessor()
            }
    
    @staticmethod
    def get_instance():
        if RentalSystem._instance is None:
            RentalSystem()
        return RentalSystem._instance
    
    def add_car(self, car):
        self.cars[car.license_plate]=  car
    
    def remove_car(self, car:Car):
        self.cars.pop(car.license_plate, None)
    
    def search_car(self, make, model, start_date, end_date):
        available_cars = []
        for car in self.cars.values():
            #customer choice
            if car.make.lower() == make.lower() and car.model.lower() == model.lower and car.available:
                #choice pruned as per availability against reservation
                if self.is_car_available(car, start_date, end_date):
                    available_cars.append(car)
        return available_cars
    
    def is_car_available(self, car, start_date, end_date):
        for reservation in self.reservations.values():
            if reservation.get_car() == car:
                if start_date < self.reservation.get_end_date() and end_date > self.reservation.get_start_date():
                    return False
        return True
    
    def make_reservation(self, customer:Customer, car, start_date, end_date):
        if self.is_car_available(car, start_date, end_date):
            reservation_id = self.generate_reservation_id()
            reservation = Reservation(reservation_id, customer, car, start_date, end_date)
            self.reservations[reservation_id] = reservation
            car.is_available = False
            return reservation
        return None

    def cancel_reservation(self, reservation_id):
        reservation = self.reservations.pop(reservation_id, None)
        if reservation is not None:
            reservation.get_car().is_available = True
    
    def process_payment(self, reservation_id, payment_method):
        return self.payment_processors[payment_method].process_payment(self.reservations[reservation_id].get_total_price())
    
    def generate_reservation_id(self):
        return "RES" + str(uuid.uuid4())[:8].upper()