
class Customer:
    def __init__(self, db, cusname,address,email,mobile,username,password):
        self.db = db
        self.cusname = cusname
        self.address = address
        self.email = email
        self.mobile = mobile        
        self.username = username
        self.password = password

    def add(self):
        query = "INSERT INTO customer (cusname,address,email,mobile,username,password) VALUES (?, ?, ?, ?, ?, ?)"
        self.db.execute_query(query, (self.cusname,self.address, self.email,self.mobile, self.username, self.password))

    def loginC(self):
        query = "SELECT id FROM customer WHERE username = ? AND password = ?"
        return self.db.fetch_one(query, (self.username, self.password))