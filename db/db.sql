-- Crear la base de datos
CREATE DATABASE hotel_soap;

-- Cambiar al esquema de trabajo
\c hotel_soap;

-- Crear la tabla availability
CREATE TABLE availability (
    room_id SERIAL PRIMARY KEY,
    room_type VARCHAR(50) NOT NULL,
    available_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Insertar datos de prueba
INSERT INTO availability (room_type, available_date, status)
VALUES 
    ('Single', '2024-12-20', 'available'),
    ('Single', '2024-12-21', 'available'),
    ('Double', '2024-12-20', 'maintenance'),
    ('Suite', '2024-12-20', 'available');

-- Crear la base de datos
CREATE DATABASE hotel_rest;

-- Cambiar al esquema de trabajo
\c hotel_rest;

-- Crear la tabla reservations
CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    room_number INT NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Confirmed'
);

-- Insertar datos de prueba
INSERT INTO reservations (room_number, customer_name, start_date, end_date)
VALUES 
    (101, 'John Doe', '2024-12-20', '2024-12-22'),
    (102, 'Jane Smith', '2024-12-23', '2024-12-25');

-- Crear la base de datos
CREATE DATABASE hotel_inventory;

-- Cambiar al esquema de trabajo
\c hotel_inventory;

-- Crear la tabla rooms
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_number INT NOT NULL UNIQUE,
    room_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Insertar datos de prueba
INSERT INTO rooms (room_number, room_type, status)
VALUES 
    (101, 'Single', 'available'),
    (102, 'Double', 'occupied'),
    (103, 'Suite', 'maintenance');
