from datetime import datetime

class Rental:
    def __init__(self, db, car_id,user_id,start_date, end_date,cus_username,approved='N', rental_id=None):
        self.db = db
        self.car_id = car_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.cus_username=cus_username
        self.approved = approved
        self.rental_id = rental_id
        

    def book(self):
        query = "INSERT INTO rentals (car_id,user_id, start_date, end_date,cus_username, approved) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.execute_query(query, (self.car_id,self.user_id,self.start_date, self.end_date,self.cus_username, self.approved))

    def approve(self,approved,rental_id):
        query = """UPDATE rentals SET approved = ? WHERE approved= ? AND id = ? """
        self.db.execute_query(query, (approved,'N',rental_id))
        
    @staticmethod
    def view_pending(db):
        query = "SELECT * FROM rentals WHERE approved = 'N'"
        return db.fetch_all(query)


    @staticmethod
    def calculate_fee(car_id, start_date, end_date, db):
        query = "SELECT min_rent_period, max_rent_period FROM cars WHERE id = ?"
        car = db.fetch_one(query, (car_id,))
        min_period, max_period = car
        rental_days = (datetime.strptime(end_date, '%d/%m/%Y') - datetime.strptime(start_date, '%d/%m/%Y')).days
        if rental_days < min_period:
            return "Rental period is less than minimum allowed."
        if rental_days > max_period:
            return "Rental period exceeds maximum allowed."
