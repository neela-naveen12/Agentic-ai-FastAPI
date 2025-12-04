
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="students api")

# dummy database 

students =[
    {"id": 1, "name": "Neela Naveen", "age": 22},
    {"id": 2, "name": "Ravi Kumar", "age": 23}
]

# 1. read all students 

@app.get("/students")
def get_all_students():
    return students

# 2 read sigle students by id 

@app.get("/student/{student_id}")
def get_by_id(student_id:int):
    for stu in students:
        if stu["id"] == student_id:
            return stu
    raise HTTPException(status_code=404,detail="student not found")

# 3. create studengt by using post method 

@app.post("/students")
def add_student(student:dict):
    student["id"] = len(students)+1
    students.append(student)
    return{
        "messege":"student added successfully !",
        "data":student
    }

# update students using put method 

@app.put("/students/{student_id}")
def update_student(student_id:int,updated:dict):
    for i,stud in enumerate(students):
        if stud["id"] == student_id:
            updated["id"] = student_id
            students[i] = updated
            return{
                "messege":"student updated succesfully!",
                "data":updated
            }
        
    raise HTTPException(status_code=404,detail="student found already")


# delete student using delete method 
@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    for stud in students:
        if stud["id"] == student_id:
            students.remove(stud)
            return{
                "messege":"student delete sucessfully!"
            }
    raise HTTPException(status_code=404,detail="student not found")