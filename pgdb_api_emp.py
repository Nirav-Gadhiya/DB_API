from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import psycopg2
import logging
from datetime import datetime

# FastAPI instance
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Define the PostgreSQL connection parameters
hostname = 'localhost'
database = 'test_db'
username = 'postgres'
password = 'vision'
port = '5432'

# Function to get the PostgreSQL connection
def get_db_connection():
    connection = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )
    return connection

# Pydantic model for employee data
class Employee(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    hire_date: str
    department: str
    salary: float

# FastAPI route to get all employees
@app.get("/employees/", response_model=List[Employee])
async def get_employees():
    try:
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        logging.debug("Fetching data from employees table.")
        cursor.execute("SELECT employee_id, first_name, last_name, hire_date, department, salary FROM employees;")
        rows = cursor.fetchall()

        if not rows:
            logging.debug("No data found in employees table.")

        # Convert rows to Employee objects
        employees = []
        for row in rows:
            employees.append(Employee(
                employee_id=row[0],
                first_name=row[1],
                last_name=row[2],
                hire_date=row[3].strftime('%Y-%m-%d'),  # Format date
                department=row[4],
                salary=row[5]
            ))

        # Close the database connection
        cursor.close()
        connection.close()

        return employees

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return {"error": "Failed to fetch data from the database"}

# FastAPI route to get employees by department
@app.get("/employees/{department}", response_model=List[Employee])
async def get_employees_by_department(department: str):
    try:
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        logging.debug(f"Fetching employees in the {department} department.")
        cursor.execute("SELECT employee_id, first_name, last_name, hire_date, department, salary FROM employees WHERE department = %s;", (department,))
        rows = cursor.fetchall()

        if not rows:
            logging.debug(f"No employees found in {department} department.")

        # Convert rows to Employee objects
        employees = []
        for row in rows:
            employees.append(Employee(
                employee_id=row[0],
                first_name=row[1],
                last_name=row[2],
                hire_date=row[3].strftime('%Y-%m-%d'),  # Format date
                department=row[4],
                salary=row[5]
            ))

        # Close the database connection
        cursor.close()
        connection.close()

        return employees

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return {"error": "Failed to fetch data from the database"}
