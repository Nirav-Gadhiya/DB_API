from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import motor.motor_asyncio
from datetime import datetime

# FastAPI instance
app = FastAPI()

# MongoDB connection
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
db = client['test_db']  # Use the existing database
employees_collection = db['employees']  # Access the 'employees' collection

# Pydantic model for the Employee
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
    employees = []
    async for employee in employees_collection.find():
        # Convert the MongoDB document to a Pydantic model
        employees.append(Employee(
            employee_id=employee['employee_id'],
            first_name=employee['first_name'],
            last_name=employee['last_name'],
            hire_date=employee['hire_date'].strftime('%Y-%m-%d'),  # Format the date as string
            department=employee['department'],
            salary=employee['salary']
        ))
    return employees

# FastAPI route to get employees by department
@app.get("/employees/{department}", response_model=List[Employee])
async def get_employees_by_department(department: str):
    employees = []
    async for employee in employees_collection.find({"department": department}):
        employees.append(Employee(
            employee_id=employee['employee_id'],
            first_name=employee['first_name'],
            last_name=employee['last_name'],
            hire_date=employee['hire_date'].strftime('%Y-%m-%d'),
            department=employee['department'],
            salary=employee['salary']
        ))
    return employees
