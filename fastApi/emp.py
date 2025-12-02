
from fastapi import FastAPI
import json

app = FastAPI()

# Load JSON file
def load_employees():
    with open("employees.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/employees")
def get_all_employees():
    employees = load_employees()
    return {
        "message": "Employee List",
        "total": len(employees),
        "data": employees
    }

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    employees = load_employees()
    for emp in employees:
        if emp["id"] == emp_id:
            return {
                "message": "Employee Found",
                "data": emp
            }
    return {"message": "Employee Not Found"}
