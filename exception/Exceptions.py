class CarNotFoundException(Exception):
    def __init__(self, message="Car not found!"):
        self.message = message
        super().__init__(self.message)

class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease not found!"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found!"):
        self.message = message
        super().__init__(self.message)
