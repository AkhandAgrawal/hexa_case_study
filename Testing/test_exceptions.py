import pytest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from exceptions.custom_exceptions import CarNotFoundException, CustomerNotFoundException, LeaseNotFoundException

def test_customer_not_found_exception():
    service_provider = ICarLeaseRepositoryImpl()
    
    with pytest.raises(CustomerNotFoundException):
        service_provider.find_customer_by_id(999) 

def test_car_not_found_exception():
    service_provider = ICarLeaseRepositoryImpl()
    
    with pytest.raises(CarNotFoundException):
        service_provider.find_car_by_id(999) 

def test_lease_not_found_exception():
    service_provider = ICarLeaseRepositoryImpl()
    
    with pytest.raises(LeaseNotFoundException):
        service_provider.return_car(999) 
