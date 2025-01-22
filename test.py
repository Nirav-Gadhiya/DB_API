from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']  # Use the existing database
employees_collection = db['employees']  # Access the existing 'employees' collection

# Sample data to insert into the 'employees' collection
employees_data = [
    {
        "employee_id": 101,
        "first_name": "John",
        "last_name": "Doe",
        "hire_date": datetime.strptime("2020-03-15", "%Y-%m-%d"),
        "department": "Engineering",
        "salary": 75000
    },
    {
        "employee_id": 102,
        "first_name": "Jane",
        "last_name": "Smith",
        "hire_date": datetime.strptime("2019-08-10", "%Y-%m-%d"),
        "department": "Marketing",
        "salary": 65000
    },
    {
        "employee_id": 103,
        "first_name": "Alice",
        "last_name": "Johnson",
        "hire_date": datetime.strptime("2021-01-25", "%Y-%m-%d"),
        "department": "Sales",
        "salary": 60000
    },
    {
        "employee_id": 104,
        "first_name": "Bob",
        "last_name": "Williams",
        "hire_date": datetime.strptime("2018-11-30", "%Y-%m-%d"),
        "department": "Engineering",
        "salary": 80000
    },
    {
        "employee_id": 105,
        "first_name": "Charlie",
        "last_name": "Brown",
        "hire_date": datetime.strptime("2022-06-01", "%Y-%m-%d"),
        "department": "HR",
        "salary": 55000
    },
    {
        "employee_id": 106,
        "first_name": "Emily",
        "last_name": "Davis",
        "hire_date": datetime.strptime("2020-09-12", "%Y-%m-%d"),
        "department": "Marketing",
        "salary": 72000
    },
    {
        "employee_id": 107,
        "first_name": "David",
        "last_name": "Martinez",
        "hire_date": datetime.strptime("2021-04-05", "%Y-%m-%d"),
        "department": "Sales",
        "salary": 67000
    },
    {
        "employee_id": 108,
        "first_name": "Sophia",
        "last_name": "Taylor",
        "hire_date": datetime.strptime("2017-12-18", "%Y-%m-%d"),
        "department": "Engineering",
        "salary": 90000
    },
    {
        "employee_id": 109,
        "first_name": "William",
        "last_name": "Anderson",
        "hire_date": datetime.strptime("2021-03-20", "%Y-%m-%d"),
        "department": "HR",
        "salary": 56000
    },
    {
        "employee_id": 110,
        "first_name": "Olivia",
        "last_name": "Wilson",
        "hire_date": datetime.strptime("2020-07-11", "%Y-%m-%d"),
        "department": "Finance",
        "salary": 77000
    }
]

# Insert the data into the 'employees' collection
employees_collection.insert_many(employees_data)

print("Employees data inserted successfully!")
