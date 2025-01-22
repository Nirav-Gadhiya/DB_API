CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    department VARCHAR(50),
    salary NUMERIC
);
-- Insert employee data into employees table
INSERT INTO employees (first_name, last_name, hire_date, department, salary)
VALUES
    ('John', 'Doe', '2020-03-15', 'Engineering', 75000),
    ('Jane', 'Smith', '2019-08-10', 'Marketing', 65000),
    ('Alice', 'Johnson', '2021-05-22', 'Sales', 58000),
    ('Bob', 'Williams', '2018-11-05', 'Human Resources', 72000),
    ('Charlie', 'Brown', '2020-01-12', 'Engineering', 80000),
    ('David', 'Davis', '2017-06-17', 'Marketing', 68000),
    ('Emma', 'Miller', '2022-03-08', 'Sales', 59000),
    ('Frank', 'Moore', '2019-07-19', 'Engineering', 74000),
    ('Grace', 'Taylor', '2021-09-10', 'Human Resources', 71000),
    ('Henry', 'Anderson', '2020-02-25', 'Marketing', 67000);
select * from employees;
