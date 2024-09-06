
class Car:
    def __init__(self, db, make, model, year, mileage, available_now, min_rent_period, max_rent_period, daily_charge, car_id=None):
        self.db = db
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period
        self.daily_charge = daily_charge
        self.car_id = car_id

    def add(self):
        query = """INSERT INTO cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period, daily_charge)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        self.db.execute_query(query, (self.make, self.model, self.year, self.mileage, self.available_now, self.min_rent_period, self.max_rent_period, self.daily_charge))

    def update(self):
        query = """UPDATE cars SET make = ?, model = ?, year = ?, mileage = ?, available_now = ?, min_rent_period = ?, max_rent_period = ?, daily_charge = ?
                   WHERE id = ?"""
        self.db.execute_query(query, (self.make, self.model, self.year, self.mileage, self.available_now, self.min_rent_period, self.max_rent_period,self.daily_charge,self.car_id))

    def upavailable(self):
        query = """UPDATE cars SET available_now = ?
                   WHERE id = ?"""
        self.db.execute_query(query, ('N',self.car_id))


    def delete(self):
        query = "DELETE FROM cars WHERE id = ?"
        self.db.execute_query(query, (self.car_id,))

    #get all the cars
    def view_all(db):
        query = "SELECT * FROM cars"
        return db.fetch_all(query)

    #get all available cars
    def view_available(db):
        query = "SELECT * FROM cars WHERE available_now = 'Y'"
        return db.fetch_all(query)

    #get all approved cars
    def view_approved(db,username):
        query = "SELECT * FROM rentals WHERE approved= ? AND cus_username= ?"
        return db.fetch_all(query,('Y',username,))
      

   #calculate daily charge
    def get_daily_charge(db, car_id):
     
        query = "SELECT daily_charge FROM cars WHERE id = ?"
        result = db.fetch_one(query, (car_id,))
        if result is not None:
            return result[0]
        else:
            print(f"No car found with ID {car_id}")
            return None

