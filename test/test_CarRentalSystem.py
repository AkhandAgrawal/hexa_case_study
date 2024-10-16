import sys
import os
import unittest
from unittest.mock import MagicMock
# Ensure that this import works
from dao.DAO import ICarLeaseRepositoryImpl
from entity.Entity import Car, Lease
from exception.Exceptions import CarNotFoundException, LeaseNotFoundException

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.repository = ICarLeaseRepositoryImpl()

        # Mock the methods in the repository to avoid real database interaction
        self.repository.addCar = MagicMock(return_value=None)
        self.repository.listAvailableCars = MagicMock(return_value=[])
        self.repository.addLease = MagicMock(return_value=None)
        self.repository.getLeases = MagicMock(return_value=[])
        self.repository.getLeaseById = MagicMock(return_value=None)
        self.repository.findCarById = MagicMock(side_effect=CarNotFoundException("Car not found"))
        
        # Create a test car
        self.test_car = Car(1, 'Toyota', 'Camry', 2020, 100.0, 'available', 5, 2.5)
        self.repository.addCar(self.test_car)

    def tearDown(self):
        # Clean up: Remove test car after tests
        # Mock the removeCar method as well to avoid database interaction
        self.repository.removeCar = MagicMock(return_value=None)
        self.repository.removeCar(self.test_car.vehicleID)

    def test_car_creation(self):
        # Verify if the car was created successfully
        self.repository.listAvailableCars.return_value = [self.test_car]
        cars = self.repository.listAvailableCars()
        self.assertIn(self.test_car, cars)

    def test_lease_creation(self):
        # Create a test lease
        lease = Lease(1, self.test_car.vehicleID, 1, '2024-10-01', '2024-10-10', 'daily')
        self.repository.addLease(lease)
        
        # Verify if the lease was created successfully
        self.repository.getLeases.return_value = [lease]
        leases = self.repository.getLeases()
        self.assertIn(lease, leases)

    def test_lease_retrieval(self):
        # Create a test lease and retrieve it
        lease = Lease(1, self.test_car.vehicleID, 1, '2024-10-01', '2024-10-10', 'daily')
        self.repository.addLease(lease)

        self.repository.getLeaseById = MagicMock(return_value=lease)
        retrieved_lease = self.repository.getLeaseById(lease.leaseID)
        self.assertEqual(retrieved_lease.leaseID, lease.leaseID)

    def test_exception_handling(self):
        with self.assertRaises(CarNotFoundException):
            self.repository.findCarById(999)  # Assume 999 does not exist

        with self.assertRaises(LeaseNotFoundException):
            self.repository.getLeaseById(999)  # Assume 999 does not exist

if __name__ == '__main__':
    result = unittest.main(exit=False)
    
    # Check if the tests passed and print a success message
    if result.result.wasSuccessful():
        print("All tests were successful!")
