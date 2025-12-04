
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
doctors = [
    {"id": 1, "name": "Dr. Ramesh", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Sita", "specialization": "Dermatologist"},
]

# get all doctors 

@app.get("/doctors")
def get_all_doctors():
    return doctors

# get doctors by id 

@app.get("/doctors/{doctor_id}")
def get_by_id(doctor_id:int):
    for doc in doctors:
        if doc["id"] == doctor_id:
            return doc
    raise HTTPException(status_code=4002,detail="doctor not found")

# add doctors post

@app.post("/doctors")
def add_doctor(new_doct:dict):
    new_doct["id"] = len(doctors)+1
    doctors.append(new_doct)
    return new_doct

# update using put

@app.put("/doctors/{doctor_id}")
def  update_doctor(doctor_id:int,update_doc:dict):
    for i, doct in enumerate(doctors):
        if doct["id"] ==doctor_id:
            update_doc["id"] = doctor_id
            doctors[i] = update_doc
            return update_doc
        
    raise HTTPException(status_code=404,detail="not found")

# delete

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id:int):
    for doc in doctors:
        if doc["id"] == doctor_id:
            doctors.remove(doc)
            return{
                "messege":"succesfully deleted"
            }
    raise HTTPException(status_code=404,detail="not found")



# Pydantic model
class Student(BaseModel):
    name: str
    age: int
    grade: str

# Storage list
students = []


@app.post("/student")
def up_student(st: Student):
    st_data = st.dict()              # convert to dict
    st_data["id"] = len(students) + 1  # create id
    students.append(st_data)
    return st_data



@app.get("/student")
def get_students():
    return students