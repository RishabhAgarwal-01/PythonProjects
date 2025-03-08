class Car:
    def __init__(self, make, model, year, license_plate, rental_price_per_day):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.rental_price_per_day = rental_price_per_day
        self.available = True # True if the car is available for rent, False otherwise
    
    @property
    def get_rental_price_per_day(self):
        return self.rental_price_per_day
    
    @property
    def get_make(self):
        return self.make
    
    @property
    def get_model(self):
        return self.model
    
    @property
    def get_year(self):
        return self.year
    
    @property
    def get_license_plate(self):
        return self.license_plate
    
    @property
    def is_available(self):
        return self.available
    
    # Setter for the is_available property
    @is_available.setter
    def is_available(self, available):
        self.available = available