import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from entity.model import Vehicle, Customer, Lease, Payment
from dao import icar_lease_repository_impl


class CarLeaseMenu:
    def __init__(self):
        self.repoimpl = icar_lease_repository_impl.ICarLeaseRepositoryImpl()

    def display_menu(self):
        print("\nCar Rental System Menu:")
        print("1. Add a New Car")
        print("2. Remove a Car")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("6. Add a New Customer")
        print("7. Remove a Customer")
        print("8. List Customers")
        print("9. Find Customer by ID")
        print("10. Create a Lease")
        print("11. Return a Leased Car")
        print("12. List Active Leases")
        print("13. List Lease History")
        print("14. Record Payment")
        print("15. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your Choice: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.remove_car()
            elif choice == '3':
                self.list_available_cars()
            elif choice == '4':
                self.list_rented_cars()
            elif choice == '5':
                self.find_car_by_id()
            elif choice == '6':
                self.add_customer()
            elif choice == '7':
                self.remove_customer()
            elif choice == '8':
                self.list_customers()
            elif choice == '9':
                self.find_customer_by_id()
            elif choice == '10':
                self.create_lease()
            elif choice == '11':
                self.return_car()
            elif choice == '12':
                self.list_active_leases()
            elif choice == '13':
                self.list_lease_history()
            elif choice == '14':
                self.record_payment()
            elif choice == '15':
                print("\nExiting...")
                self.repoimpl.closeconn()
                break
            else:
                print("Invalid Choice. Please try again.")


    def add_car(self):
        make = input("Enter Company Name: ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        daily_rate = float(input("Enter Daily Rate: "))
        available = input("Enter Status (available, notAvailable): ")
        passenger_capacity = int(input("Enter Passenger Capacity: "))
        engine_capacity = float(input("Enter Engine Capacity: "))
        vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, status=available,passenger_capacity=passenger_capacity, engine_capacity=engine_capacity)
        self.repoimpl.add_car(vehicle)


    def remove_car(self):
        Vehicle_id=int(input("Enter Vechicle ID: "))
        self.repoimpl.remove_car(Vehicle_id)


    def list_available_cars(self):
       available_cars= self.repoimpl.list_available_cars()
       if(available_cars == []):
        print("Available Cars Not Found!")
       else:
            for car in available_cars:
                print("Vehicle ID:", car.get_vehicle_id())
                print("Make:", car.get_make())
                print("Model:", car.get_model())
                print("Year:", car.get_year())
                print("Daily Rate:", car.get_daily_rate())
                print("Status:", car.get_status())
                print("Passenger Capacity:", car.get_passenger_capacity())
                print("Engine Capacity:", car.get_engine_capacity())
                print() 
        

    def list_rented_cars(self):

        rented_cars= self.repoimpl.list_rented_cars()
        if(rented_cars == []):
            print("Available Cars Not Found!")
        else:
            for car in rented_cars:
                print("Vehicle ID:", car.get_vehicle_id())
                print("Make:", car.get_make())
                print("Model:", car.get_model())
                print("Year:", car.get_year())
                print("Daily Rate:", car.get_daily_rate())
                print("Status:", car.get_status())
                print("Passenger Capacity:", car.get_passenger_capacity())
                print("Engine Capacity:", car.get_engine_capacity())
                print()
        

    def find_car_by_id(self):
        vehicle_id=int(input("Enter Vehicle ID: "))
        car=self.repoimpl.find_car_by_id(vehicle_id)
        if car:
            print("Vehicle ID:", car.get_vehicle_id())
            print("Make:", car.get_make())
            print("Model:", car.get_model())
            print("Year:", car.get_year())
            print("Daily Rate:", car.get_daily_rate())
            print("Available:", car.get_status())
            print("Passenger Capacity:", car.get_passenger_capacity())
            print("Engine Capacity:", car.get_engine_capacity())
            print()
        else:
            print("Car Not Found!!")
        

    def add_customer(self):
        fname=input("Enter First Name: ")
        lname=input("Enter Last Name: ")
        email=input("Enter Email: ")
        phn=input("Enter Phone number: ")
        customer=Customer(first_name = fname,last_name=lname,email=email,phone_number=phn)
        self.repoimpl.add_customer(customer)


    def remove_customer(self):
        customer_id=int(input("Enter Customer ID: "))
        self.repoimpl.remove_customer(customer_id)
        
        
    def list_customers(self):
        customers = self.repoimpl.list_customers()
        if customers:
            print("\nList of Customers:")
            for customer in customers:
                print("Customer ID:", customer.get_customer_id())
                print("First Name:", customer.get_first_name())
                print("Last Name:", customer.get_last_name())
                print("Email:", customer.get_email())
                print("Phone Number:", customer.get_phone_number())
                print()
        else:
            print("No Customers Found!!")



    def find_customer_by_id(self):
        customer_id = int(input("\nEnter the Customer ID to Find: "))
        customer = self.repoimpl.find_customer_by_id(customer_id)
        if customer:
            print("Customer Found:")
            print("Customer ID:", customer.get_customer_id())
            print("First Name:", customer.get_first_name())
            print("Last Name:", customer.get_last_name())
            print("Email:", customer.get_email())
            print("Phone Number:", customer.get_phone_number())
        

    def create_lease(self):
            customer_id = int(input("Enter Customer ID: "))
            vehicle_id = int(input("Enter Vehicle ID: "))
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            type=input("Enter Type ('DailyLease', 'MonthlyLease'): ")
            lease=Lease(customer_id=customer_id,vehicle_id=vehicle_id,start_date=start_date,end_date=end_date,type=type)
            self.repoimpl.create_lease(lease)


    def return_car(self):
        lease_id = int(input("Enter the Lease ID to Find: "))
        lease = self.repoimpl.return_car(lease_id)
        if lease:
            print()
            print("Lease ID:", lease[0])
            print("Customer ID:", lease[1])
            print("Vehicle ID:", lease[2])
            print("Start Date:", lease[3])
            print("End Date:", lease[4]) 
            print("Type:",lease[5])
            print()
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")


    def list_active_leases(self):
        lease=self.repoimpl.list_active_leases()
        print()
        if lease:
           for i in lease:        
                print("Lease ID:", i[0])
                print("Customer ID:",i[1])
                print("Vehicle ID:", i[2])
                print("Start Date:", i[3])  
                print("End Date:", i[4])
                print("Type:", i[5])
                print()
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")
        

    def list_lease_history(self):
        lease=self.repoimpl.list_lease_history()
        print()
        if lease:
           for i in lease:         
                print("Lease ID:", i[0])
                print("Customer ID:",i[1])
                print("Vehicle ID:", i[2])
                print("Start Date:", i[3])  
                print("End Date:", i[4])
                print("Type:", i[5])
                print()
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")


    def record_payment(self):
           try:
                lease_id = int(input("Enter Lease ID: "))
                transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")
                amount = float(input("Enter Payment Amount: "))
                lease = self.repoimpl.return_car(lease_id)
                if lease:
                    pay=Payment(lease_id=lease_id, payment_date=transaction_date, amount=amount)
                    self.repoimpl.record_payment(pay)
                else:
                    print("Invalid Lease ID!!")
           except ValueError:
                print("Please Enter Valid Input for Payment ID, Lease ID, and Amount.")
           except Exception as e:
                print("Failed to Record Payment!,", str(e))

menu = CarLeaseMenu()
menu.run()
