DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    performance INT
);
