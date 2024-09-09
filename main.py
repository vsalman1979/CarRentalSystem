from clsUser import User
from clsCar import Car
from clsRental import Rental
from clsCustomer import Customer
from database import Database
from datetime import datetime
from clsfeedbacks import feedbacks

import createdb 

def main():

    createdb.create_tables()   
    db = Database()
 
    while True:

        print("\n=======================================================================================")
        print("                           WELCOME TO THE VPS CAR RENTAL COMPANY                       ")
        print("                             (Market leader in renting cars)                           ")                                
        print("=======================================================================================")
    
    
        print("\n                              1. View available cars")
        print("                              2. Customer Register")        
        print("                              3. Customer Login")
        print("                              4. Customer feedbacks")
        print("                              5. Admin Login(office use only)")
        print("                              6. Exit")
        print("                              6. Help")
        choice = input("\nChoose an option: ")

        if choice == '1':
            print("ID | Make | Model | Model | Year | Mileage | Available | Min | Max | Daily")
            cars = Car.view_all(db)
            for car in cars:
                print(car)
            
        elif choice == '2':
            global username
                 
            cusname = get_valid_input("\nCustomer name: ",str)
            address = get_valid_input("Address      : ",str)
            email   = get_valid_input("Email        : ",str)
            mobile  = get_valid_input("mobile No    : ",str)
            username= get_valid_input("username     : ",str)
            password= get_valid_input("password     : ",str)
            customer= Customer(db, cusname,address,email,mobile,username,password)
            customer.add()
            print("\nRegistration Completed!.Please press number 3 to login with user username and password.")
            

        elif choice == '3':
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            cus_data = Customer(db, any,any,any,any,username,password).loginC()

            if cus_data:
                cus_id = cus_data
                customer_menu(db,cus_id)
            else:
                print("Invalid username or password!.")
                print("(register first if you are a new customer)")

        elif choice == '4':
            feedback = feedbacks.viewfeedbacks(db)
            for cfeedback in feedback:
                print(cfeedback)
        
        
        elif choice == '5':
            global ausername
            username = input("\nEnter username: ")
            password = input("Enter password: ")

            ausername=username
            
            user_data = User(db, username, password).login()
            if user_data:
                user_id = user_data
                print(f"Logged in as Admin")
                admin_menu(db,user_id)
            else:
                print("Invalid username or password!")


        elif choice == '6':
            print("Exiting...")
            db.close()
            break

        else:
            print("Invalid option! Please try again.")

def admin_menu(db,user_id):
    while True:
        print("\nAdmin Menu      login user :" + (ausername))
        print("\n1. Add Car")
        print("2. Update")
        print("3. Delete Car")
        print("4. View All Cars")
        print("5. View Pending Rentals")
        print("6. Approve the car")
        print("7. Create User")
        print("8. Change Password")
        print("9. Logout")
        choice = input("\nChoose an option: ")

        if choice == '1':
            make = get_valid_input("Enter new car make: ",str)
            model = get_valid_input("Enter new car model: ",str)
            year = get_valid_input("Enter new car year: ", int)
            mileage = get_valid_input("Enter new car mileage: ", float)
            available_now = get_valid_input("Available now (Y/N): ",str).capitalize()
            min_rent_period = get_valid_input("Enter new minimum rent period (days): ", int)
            max_rent_period = get_valid_input("Enter new maximum rent period (days): ", int)
            daily_charge = get_valid_input("Enter new daily charge: ", float)
            
            car = Car(db, make, model, year, mileage, available_now, min_rent_period, max_rent_period, daily_charge)
            car.add()
            print("\nCar added successfully!")

        elif choice == '2':

            car_id = get_valid_input("\nEnter car ID to update: ",int)
            make = get_valid_input("Enter new car make: ",str)
            model = get_valid_input("Enter new car model: ",str)
            year = get_valid_input("Enter new car year: ", int)
            mileage = get_valid_input("Enter new car mileage: ", float)
            available_now = get_valid_input("Available now (Y/N): ",str).capitalize()
            min_rent_period = get_valid_input("Enter new minimum rent period (days): ", int)
            max_rent_period = get_valid_input("Enter new maximum rent period (days): ", int)
            daily_charge = get_valid_input("Enter new daily charge: ", float)

            car = Car(db, make, model, year, mileage, available_now, min_rent_period, max_rent_period, daily_charge, car_id)
            car.update()
            print("\nrecord updated!")

        elif choice == '3':
            car_id = int(input("Enter car ID to delete: "))
            Car(db, None, None, None, None, None, None, None, None, car_id).delete()
            print("\nCar deleted successfully!")

        elif choice == '4':
            print("ID | Make | Model | Model | Year | Mileage | Available | Min | Max | Daily")
            cars = Car.view_all(db)
            for car in cars:
                print(car)

        elif choice == '5':
            rentals = Rental.view_pending(db)
            for rental in rentals:
                print("RentId | CarId | customer | DateFrm | DateTo | Available")                
                print(rental)

        elif choice == '6':
            rental_id = input("\nEnter RentalId: ")
            approved  = input("  Approve(Y/N)  : ").capitalize()
            rental=Rental(db,None,None,None,None,None,approved,rental_id)
            print(approved,rental_id)
            rental.approve(approved,rental_id)
            print("\nrecord updated!")

        elif choice == '7':
            username=  input("username     : ")
            password = input("password     : ")
            user = User(db,password,username)
            user.register()
            print("\nUser created!")

        elif choice == '8':
            username = input("\nusername: ")
            password = input("password  : ")
            user = User(db,username,password)
            user.update()
            print("\npassword has changed!")

        elif choice == '9':
            print("Logging out...")
            break

        else:
            print("\nInvalid option! Please try again.")

def customer_menu(db,cus_id):
    while True:
        print("\nHi " + username) 
        print("\nWecome to the VPS car rentals. Please select the sutable car for you")
        print("\n1. View Available Cars")
        print("2. Book a Car")
        print("3. Check your booking status")
        print("4. Give your feedback")        
        print("5. Logout")
        choice = input("\nChoose an option: ")
        

        if choice == '1':
            cars = Car.view_available(db)
            for car in cars:
                print(car)

        elif choice == '2':
            car_id = input("\nEnter car ID to book: ")

            # Calculate the number of rental days
            start_date = get_valid_input("Enter start date (DD/MM/YYYY): ",str)
            stdate = datetime.strptime(start_date, "%d/%m/%Y")
            end_date = get_valid_input("Enter end date (DD/MM/YYYY): ",str)
            endate = datetime.strptime(end_date, "%d/%m/%Y")
            rental_days = (endate - stdate).days
                      
            # get daily rate from car class
            daily_charge = Car.get_daily_charge(db, car_id)
            if daily_charge is None:
                print("Car not found. Please check the car ID and try again.")
                continue  
            
            # Calculate amount
            total_cost = rental_days * daily_charge

            print(f"Rental Days                     :  {rental_days :.2f}")
            print(f"Daily Charge                    : ${daily_charge :.2f}")
            print("Additional Charge (Refundable)  : $100.00")
            print(f"Total cost                      : ${total_cost + 100 :.2f}")
            rental = Rental(db,1,car_id,start_date, end_date,username,'N',any)
            rental.book()
            
            car=Car(db,any,any,any,any,'N',any,any,any,car_id)
            car.upavailable()

            print(f"\nThank you for booking a car for {rental_days} day(s)!. admin will approve your request soon")
                    
        elif choice == '3':
            cars = Car.view_approved(db,username)
            
            if cars:
                print("\nHi!" + username )
                print("Your booking is approved by the admin")
            else:
                print("Sorry!" + username )
                print("Your booking is still waiting for approval!")
                       
        elif choice=='4':
             print("Hi!"+ username)
             print("Your feedbacks are very important for us.Thank you")
             feedback = input("Enter your feedback: ")
             Feedbacks=feedbacks(db,username,feedback)
             print(username,feedback)
             Feedbacks.getfeedback()
             print("\nThank you for your feedback" )
        
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid option! Please try again.")

def get_valid_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        
        if input_type == str:
            if user_input.strip() == "":
                print("INVALID! Input should not be empty.")
                continue
            return user_input
        else:
            try:
                return input_type(user_input)
            except ValueError:
                print(f"INVALID! Input should be a {input_type.__name__}")



if __name__ == "__main__":

 main()
