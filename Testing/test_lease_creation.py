import pytest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from entity.model import Lease

def test_create_lease(monkeypatch):
    service_provider = ICarLeaseRepositoryImpl()

    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: {
        "Enter Customer ID: ": 101,
        "Enter Vehicle ID: ": 201,
        "Enter Start Date (YYYY-MM-DD): ": "2024-11-01",
        "Enter End Date (YYYY-MM-DD): ": "2024-11-10",
        "Enter Type('DailyLease', 'MonthlyLease'): ": "DailyLease"
    }[_.strip()])

    lease = Lease(customer_id=101, vehicle_id=201, start_date="2024-11-01", end_date="2024-11-10", type="DailyLease")
    lease_created = service_provider.create_lease(lease)

    assert lease_created is None  
