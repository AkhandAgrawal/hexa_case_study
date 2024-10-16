CREATE DATABASE Car_Rental_System;
USE Car_Rental_System;

CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY ,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate INT,
    status VARCHAR(15),
    passengerCapacity INT,
    engineCapacity INT
);
CREATE TABLE Customer (
    customerID INT PRIMARY KEY ,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    phoneNumber VARCHAR(20)
);
CREATE TABLE Lease (
    leaseID INT PRIMARY KEY,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(15),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);
CREATE TABLE Payment (
    paymentID INT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount INT,
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);
