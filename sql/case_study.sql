create database CaseStudyCRS;
use CaseStudyCRS;

CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY Identity(1,1),
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate DECIMAL(10, 2),
    status VARCHAR(15) CHECK (status IN ('available', 'notAvailable')),
    passengerCapacity INT,
    engineCapacity DECIMAL(10, 2)
);

CREATE TABLE Customer (
    customerID INT PRIMARY KEY identity(100,1),
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100),
    phoneNumber VARCHAR(15)
);

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY identity(300,1),
    vehicleID INT FOREIGN KEY REFERENCES Vehicle(vehicleID),
    customerID INT FOREIGN KEY REFERENCES Customer(customerID),
    startDate DATE,
    endDate DATE,
    type VARCHAR(50) CHECK (type IN ('DailyLease', 'MonthlyLease'))
);

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY identity(1000,1),
    leaseID INT FOREIGN KEY REFERENCES Lease(leaseID),
    paymentDate DATE,
    amount DECIMAL(10, 2)
);



INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
VALUES 
('Tata', 'Nexon', 2022, 1200.50, 'available', 5, 1.2),
('Maruti', 'Swift', 2020, 1000.00, 'notAvailable', 5, 1.2),
('Mahindra', 'XUV500', 2021, 2000.75, 'available', 7, 2.2),
('Hyundai', 'Creta', 2023, 1800.30, 'available', 5, 1.6),
('Honda', 'City', 2019, 1500.00, 'available', 5, 1.5),
('Kia', 'Seltos', 2024, 1750.00, 'notAvailable', 5, 1.6),
('Renault', 'Duster', 2020, 1600.50, 'available', 5, 1.5),
('Toyota', 'Innova', 2022, 2500.00, 'available', 7, 2.5),
('Ford', 'Ecosport', 2019, 1400.50, 'notAvailable', 5, 1.5),
('Volkswagen', 'Polo', 2020, 1100.00, 'available', 5, 1.0),
('MG', 'Hector', 2022, 2200.00, 'available', 5, 2.0),
('Nissan', 'Kicks', 2021, 1700.30, 'notAvailable', 5, 1.5),
('Skoda', 'Rapid', 2024, 1300.00, 'available', 5, 1.6),
('Jeep', 'Compass', 2022, 2600.75, 'available', 5, 2.0),
('Audi', 'Q5', 2024, 4500.00, 'available', 5, 2.5);



INSERT INTO Customer (firstName, lastName, email, phoneNumber)
VALUES 
('Harshwardhan', 'Songirkar', 'harsh20wardhan@gmail.com', '9098491788'),
('Yash', 'Agrawal', 'sde.yash.agrawal@gmail.com', '6263605421'),
('Sarthak', 'Londhey', 'sarthak.londhey@gmail.com', '9826996453'),
('Khushi', 'Joshi', 'khushijoshi0129@gmail.com', '8770108627'),
('Suresh', 'Kumar', 'suresh.kumar@gmail.com', '9876543214'),
('Megha', 'Verma', 'megha.verma@gmail.com', '9876543215'),
('Rahul', 'Mishra', 'rahul.mishra@gmail.com', '9876543216'),
('Neha', 'Jain', 'neha.jain@gmail.com', '9876543217'),
('Aman', 'Rathore', 'aman.rathore@gmail.com', '9876543218'),
('Richa', 'Desai', 'richa.desai@gmail.com', '9876543219'),
('Sanjay', 'Gupta', 'sanjay.gupta@gmail.com', '9876543220'),
('Sneha', 'Joshi', 'sneha.joshi@gmail.com', '9876543221'),
('Raj', 'Malhotra', 'raj.malhotra@gmail.com', '9876543222'),
('Priya', 'Iyer', 'priya.iyer@gmail.com', '9876543223'),
('Abhishek', 'Tiwari', 'abhishek.tiwari@gmail.com', '9876543224');



INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type)
VALUES 
(1, 100, '2023-01-05', '2023-01-10', 'MonthlyLease'),
(2, 101, '2023-02-10', '2023-02-20', 'MonthlyLease'),
(3, 102, '2023-03-15', '2023-03-18', 'DailyLease'),
(4, 103, '2023-04-01', '2023-04-30', 'MonthlyLease'),
(5, 104, '2023-05-07', '2023-05-10', 'MonthlyLease'),
(6, 105, '2023-06-10', '2023-06-20', 'DailyLease'),
(7, 106, '2023-07-15', '2023-07-17', 'DailyLease'),
(8, 107, '2023-08-01', '2023-08-30', 'MonthlyLease'),
(9, 108, '2023-09-05', '2023-09-10', 'MonthlyLease'),
(10, 109, '2023-10-12', '2023-10-22', 'MonthlyLease'),
(11, 110, '2023-11-01', '2023-11-03', 'DailyLease'),
(12, 111, '2023-12-10', '2023-12-20', 'MonthlyLease'),
(13, 112, '2023-01-12', '2023-01-15', 'DailyLease'),
(14, 113, '2023-02-25', '2023-03-05', 'MonthlyLease'),
(15, 114, '2023-03-15', '2023-03-18', 'DailyLease');




INSERT INTO Payment (leaseID, paymentDate, amount)
VALUES 
(300, '2023-01-10', 6000.00),
(301, '2023-02-20', 20000.00),
(302, '2023-03-18', 6002.25),
(303, '2023-04-30', 18000.00),
(304, '2023-05-10', 4500.00),
(305, '2023-06-20', 19500.50),
(306, '2023-07-17', 5100.50),
(307, '2023-08-30', 25000.00),
(308, '2023-09-10', 8500.75),
(309, '2023-10-22', 22000.00),
(310, '2023-11-03', 9000.25),
(311, '2023-12-20', 15000.75),
(312, '2023-01-15', 4000.00),
(313, '2023-03-05', 18000.00),
(314, '2023-03-18', 5100.25);

select * from Payment;
select * from Vehicle;
select * from Lease;
select * from Customer;
