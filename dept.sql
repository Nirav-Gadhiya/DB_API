CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    head_of_department VARCHAR(100)
);
INSERT INTO departments (department_name, location, head_of_department)
VALUES
    ('Engineering', 'San Francisco', 'Alice Johnson'),
    ('Marketing', 'New York', 'Bob Smith'),
    ('Sales', 'Chicago', 'Charlie Brown');
select * from departments;