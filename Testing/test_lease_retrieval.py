from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl

def test_retrieve_lease():
    service_provider = ICarLeaseRepositoryImpl()
    
    lease_id = 301 
    retrieved_lease = service_provider.return_car(lease_id)
    
    assert retrieved_lease is not None  
