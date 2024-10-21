import pytest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from entity.model import Vehicle

def test_create_car(monkeypatch):
    service_provider = ICarLeaseRepositoryImpl()

    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: {
        "Enter Company Name: ": "Honda",
        "Enter Model: ": "Civic",
        "Enter Year: ": 2021,
        "Enter Daily Rate: ": 120.0,
        "Enter Status (available, notAvailable): ": "available",
        "Enter Passenger Capacity: ": 5,
        "Enter Engine Capacity: ": 1.8
    }[_.strip()])

    car = Vehicle(make="Honda", model="Civic", year=2021, daily_rate=120.0, status="available", passenger_capacity=5, engine_capacity=1.8)
    car_id = service_provider.add_car(car)

    assert car_id is None  # Change this based on your actual implementation
