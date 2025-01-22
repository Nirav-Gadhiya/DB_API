import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

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

connection = None

# Define the Pydantic model for the departments table data
class Department(BaseModel):
    department_id: int
    department_name: str
    location: str
    head_of_department: str

# Function to connect to the PostgreSQL database
def get_db_connection():
    connection = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )
    return connection

# FastAPI route to get departments data
@app.get("/departments/", response_model=List[Department])
async def get_departments():
    try:
        # Create a connection to the database
        connection = get_db_connection()
        cursor = connection.cursor()

        logging.debug("Fetching data from departments table.")
        cursor.execute("SELECT department_id, department_name, location, head_of_department FROM departments;")
        rows = cursor.fetchall()

        if not rows:
            logging.debug("No data found in departments table.")
        
        # Convert the rows to a list of Department objects
        departments = []
        for row in rows:
            departments.append(Department(
                department_id=row[0],
                department_name=row[1],
                location=row[2],
                head_of_department=row[3]
            ))

        # Close the database connection
        cursor.close()
        connection.close()

        # Return the data as a JSON response
        logging.debug("Returning data.")
        return departments

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return {"error": "Failed to fetch data from the database"}
