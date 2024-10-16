import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.DAO import ICarLeaseRepositoryImpl
from entity.Entity import Car
import sys

if __name__ == "__main__":
    try:
        repository = ICarLeaseRepositoryImpl()
        
        # Adding a car
        car = Car(1, 'Toyota', 'Camry', 2020, 100.0, 'available', 5, 2.5)
        repository.addCar(car)
        print("Car added successfully!")

        # List available cars
        cars = repository.listAvailableCars()
        for car in cars:
            print(car)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
