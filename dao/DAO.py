from util.Util import DBConnUtil
from entity.Entity import Car

class ICarLeaseRepositoryImpl:
    def __init__(self):
        self.conn = DBConnUtil.create_db_connection()

    def addCar(self, car):
        cursor = self.conn.cursor()
        query = "INSERT INTO Vehicle (vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, car.vehicleID, car.make, car.model, car.year, car.dailyRate, car.status, car.passengerCapacity, car.engineCapacity)
        self.conn.commit()

    def listAvailableCars(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Vehicle WHERE status = 'available'"
        cursor.execute(query)
        return cursor.fetchall()
