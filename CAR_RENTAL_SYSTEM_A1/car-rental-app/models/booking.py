class Booking:
    def __init__(self,booking_id, car_id,model,name,user_id, start_date, end_date, rental_status,price,registration_number):
        self.booking_id = booking_id
        self.car_id = car_id
        self.model = model
        self.name = name
        self.user_id = user_id
        self.registration_number = registration_number
        self.start_date = start_date
        self.end_date = end_date
        self._rental_status = rental_status
        self._price = price

    #getter setter for rental status
    def get_rental_status(self):
        return self._rental_status
    
    def set_rental_status(self, value):
        self._rental_status = value

    #getter setter for price
    def get_price(self):
        return self._price
    
    def set_price(self, value):
        self._price = value