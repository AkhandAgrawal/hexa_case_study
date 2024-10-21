class CarNotFoundException(Exception):
    def __init__(self, vehicle_id):
        super().__init__(f"Car with ID {vehicle_id} not found in the database.\n")
        self.vehicle_id = vehicle_id

class LeaseNotFoundException(Exception):
    def __init__(self, lease_id):
        super().__init__(f"Lease with ID {lease_id} not found in the database.\n")
        self.lease_id = lease_id

class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
        super().__init__(f"Customer with ID {customer_id} not found in the database.\n")
        self.customer_id = customer_id
