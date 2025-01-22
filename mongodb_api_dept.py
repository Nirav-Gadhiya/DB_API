from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import motor.motor_asyncio

# FastAPI app instance
app = FastAPI()

# Connect to the existing MongoDB database using Motor
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client['test_db']  # Connect to the existing database
departments_collection = db['departments']  # Access the existing collection

# Pydantic model for the departments
class Department(BaseModel):
    department_name: str
    location: str
    head_of_department: str

# FastAPI route to get all departments
@app.get("/departments/", response_model=List[Department])
async def get_departments():
    departments = []
    async for department in departments_collection.find():
        departments.append(Department(
            department_name=department['department_name'],
            location=department['location'],
            head_of_department=department['head_of_department']
        ))
    return departments
