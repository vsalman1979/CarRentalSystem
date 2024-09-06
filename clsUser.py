
class User:
    def __init__(self, db, username, password):
        self.db = db
        self.username = username
        self.password = password
     

    def register(self):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.db.execute_query(query,(self.username,self.password))
        print (query,(self.username,self.password)) 

    def update(self):
        query = "UPDATE users SET password = ? WHERE username= ?"
        self.db.execute_query(query, (self.password,self.username))
        print (query, (self.password,self.username))

    def login(self):
        query = "SELECT id FROM users WHERE username = ? AND password = ?"
        return self.db.fetch_one(query, (self.username, self.password))

     
        
