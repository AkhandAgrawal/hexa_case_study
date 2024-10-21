import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.model import Vehicle, Customer, Lease, Payment
from datetime import date
from dao.icar_lease_repository import ICarLeaseRepository
from exceptions.custom_exceptions import *
from util.db_conn_util import *


class ICarLeaseRepositoryImpl(ICarLeaseRepository):
   
   def __init__(self) -> None:
       self.conn = DBConnection.getConnection()
       self.cursor = self.conn.cursor()

   def add_car(self, vehicle: Vehicle) -> None:
       try:
           self.cursor.execute("""
               INSERT INTO Vehicle (make, model, year, daily_rate, status, passenger_capacity, engine_capacity) 
               VALUES (?, ?, ?, ?, ?, ?, ?);""",
               (vehicle.get_make(), vehicle.get_model(), vehicle.get_year(), 
                vehicle.get_daily_rate(), vehicle.get_status(), 
                vehicle.get_passenger_capacity(), vehicle.get_engine_capacity()))
           self.conn.commit()
           print("Vehicle Added Successfully!!\n")
       except Exception as e:
           self.conn.rollback()
           print("Error Occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def remove_car(self, vehicle_id: int) -> None:
       try:
           self.cursor.execute("DELETE FROM Vehicle WHERE vehicleID = ?;", (vehicle_id,))
           if self.cursor.rowcount == 0:
               raise CarNotFoundException(vehicle_id)
           self.conn.commit()
           print("Vehicle Removed Successfully!!\n")
       except CarNotFoundException as e:
           print(e)
       except Exception as e:
           self.conn.rollback()
           print("Error Occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def list_available_cars(self):
       try:
           available_cars = []
           self.cursor.execute("SELECT * FROM Vehicle WHERE status = 'available';")
           information = self.cursor.fetchall()
           for row in information:
               vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity = row
               vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, 
                                 status=status, passenger_capacity=passenger_capacity, 
                                 engine_capacity=engine_capacity, vehicle_id=vehicle_id)
               available_cars.append(vehicle)
           return available_cars
       except Exception as e:
           print("Error occurred while fetching available cars:", str(e))
           return []
       finally:
           print("Select the Option From Below:")

   def list_rented_cars(self): 
       try:
           rented_cars = []
           self.cursor.execute("SELECT * FROM Vehicle WHERE status != 'available';")
           for row in self.cursor.fetchall():
               vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity = row
               vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, 
                                 status=status, passenger_capacity=passenger_capacity, 
                                 engine_capacity=engine_capacity, vehicle_id=vehicle_id)
               rented_cars.append(vehicle)
           return rented_cars
       except Exception as e:
           print("Error occurred while fetching rented cars:", str(e))
           return []
       finally:
           print("Select the Option From Below:")

   def find_car_by_id(self, Vehicle_id: int) -> Vehicle:
        try:
            self.cursor.execute("""SELECT * FROM Vehicle WHERE vehicleID = ?;""", (Vehicle_id,))
            if self.cursor.rowcount == 0:
                raise CarNotFoundException(Vehicle_id)
            else:
                row = self.cursor.fetchone()
                vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity = row
                return Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, status=status,
                            passenger_capacity=passenger_capacity, engine_capacity=engine_capacity, vehicle_id=vehicle_id)
        except CarNotFoundException as e:
            print(e)
            raise  
        except Exception as e:
            print("Error occurred,", str(e))
            return None
        finally:
            print("Select the Option From Below:")

   def add_customer(self, customer: Customer) -> None:
       try:
           self.cursor.execute("""
               INSERT INTO Customer (first_name, last_name, email, phone_number)
               VALUES (?, ?, ?, ?);""", 
               (customer.get_first_name(), customer.get_last_name(), 
                customer.get_email(), customer.get_phone_number()))
           self.conn.commit()
           print("Customer Added Successfully!!\n")
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def remove_customer(self, customer_id: int) -> None:
       try:
           self.cursor.execute("DELETE FROM Customer WHERE customerID = ?;", (customer_id,))
           if self.cursor.rowcount == 0:
               raise CustomerNotFoundException(customer_id)
           self.conn.commit()
           print("Customer Removed Successfully!!\n")
       except CustomerNotFoundException as e:
           print(e)
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def list_customers(self) -> list[Customer]:
       try:
           self.cursor.execute("SELECT * FROM Customer;")
           customers = []
           for row in self.cursor.fetchall():
               customer_id, first_name, last_name, email, phone_number = row
               customer = Customer(customer_id=customer_id, first_name=first_name, 
                                   last_name=last_name, email=email, phone_number=phone_number)
               customers.append(customer)
           return customers
       except Exception as e:
           print("Error occurred:", str(e))
           return []
       finally:
           print("Select the Option From Below:")

   def find_customer_by_id(self, customer_id: int) -> Customer:
        try:
            self.cursor.execute("""SELECT * FROM Customer WHERE customerID = ?;""", (customer_id,))
            if self.cursor.rowcount == 0:
                raise CustomerNotFoundException(customer_id)
            else:
                row = self.cursor.fetchone()
                customer_id, first_name, last_name, email, phone_number = row
                return Customer(customer_id=customer_id, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
        except CustomerNotFoundException as e:
            print(e)
            raise 
        except Exception as e:
            print("Error occurred,", str(e))
            return None
        finally:
            print("Select the Option From Below:")


   def create_lease(self, lease: Lease) -> Lease:
       try:
           self.cursor.execute("""
               INSERT INTO Lease (vehicle_id, customer_id, start_date, end_date, lease_type) 
               VALUES (?, ?, ?, ?, ?);""",
               (lease.get_vehicle_id(), lease.get_customer_id(), 
                lease.get_start_date(), lease.get_end_date(), lease.get_type()))
           self.conn.commit()
           print("Lease Created Successfully!!\n")
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def return_car(self, lease_id: int) -> Lease:
    try:
        self.cursor.execute("""SELECT * FROM Lease WHERE leaseID = ?;""", (lease_id,))
        row = self.cursor.fetchone()
        if row is None:
            raise LeaseNotFoundException(lease_id)
        return row
    except LeaseNotFoundException as e:
        print(e)
        raise 
    except Exception as e:
        print("Error occurred,", str(e))
        return None

   def list_active_leases(self) -> list[Lease]:
       try:
           start_date = input("Enter Start Date (YYYY-MM-DD): ")
           self.cursor.execute("SELECT * FROM Lease WHERE startDate = ?;", (start_date,))
           return self.cursor.fetchall()
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))

   def list_lease_history(self) -> list[Lease]:
       try:
           self.cursor.execute("SELECT * FROM Lease;")
           return self.cursor.fetchall()
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))

   def record_payment(self, payment: Payment) -> None:
       try:
           self.cursor.execute("""
               INSERT INTO Payment (lease_id, payment_date, amount) 
               VALUES (?, ?, ?);""",
               (payment.get_lease_id(), payment.get_payment_date(), payment.get_amount()))
           self.conn.commit()
           print("Payment Recorded Successfully!!\n")
       except Exception as e:
           self.conn.rollback()
           print("Error occurred:", str(e))
       finally:
           print("Select the Option From Below:")

   def closeconn(self):
       if hasattr(self, 'cursor'):
           self.cursor.close()
       if hasattr(self, 'conn'):
           self.conn.close()
