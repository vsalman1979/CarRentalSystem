class feedbacks:
    def __init__(self, db, cusname, feedback):
        self.db = db
        self.cusname = cusname
        self.feedback = feedback
          
    def getfeedback(self):
            query = "INSERT INTO feedbacks (cusname,feedback) VALUES (?, ?)"
            self.db.execute_query(query, (self.cusname,self.feedback))

    #get all the cars
    def viewfeedbacks(db):
        query = "SELECT * FROM feedbacks"
        return db.fetch_all(query)
