DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS animals;

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    performance INT
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    employee_id INT REFERENCES employees(id)
);