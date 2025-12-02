
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def home():
    return {'data':{'this is a home Page'}}


@app.get('/about')
def about():
    return {'data':{'this is a about page'}}

@app.get('/contact')
def contact():
    return {'data':'this is a contact page '}

@app.get('/menu')
def menu():
    return{
        "data": "list of items"
    }

# Request Body Model
class User(BaseModel):
    name: str
    age: int
    city: str

# POST API
@app.post("/create-user")
def create_user(user: User):
    return {
        "message": "User created successfully!",
        "data": user
    }

class Items(BaseModel):
    name:str
    price:int
    
@app.post("/items")
def list_items(items:Items):
    return{
        "messege": "Items are displayed"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/main/{main_name}")
def get_main(main_name:str):
    return{
        "main_name": main_name
    }

@app.get("/user/{user_id}/name/{user_name}")
def get_details(user_id:int,user_name:str):
    return{
        "user_id":user_id,
        "user_name":user_name
        
    }




@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/square/{num}")
def find_square(num:int):
    return{
        "square":num * num
    }

class Products(BaseModel):
    name:str
    id: int
@app.post("/product/{product_id}")
def product_list(product_id :int,products:Products):
    return{
        "messege":"Items created",
        "product_id":product_id,
        "product_details":products
    }

# 1. Creation of fastapi  using get method
@app.get("/home")
def Home():
    return{
        "messege": "Welcome Home"
    }

# 2. creation of fastAPI using post method

class Student(BaseModel):
    name:str
    id:int
    location:str

@app.post("/student")
def stu_d(student:Student):
    return{
        "messege":"Student DataBase Created!",
        "name":student.name,
        "id":student.id,
        "location":student.location

    }


# 2. creation of fastAPI using path get method

@app.get("/menu/{menu_id}")
def menu_list(menu_id: int):
    return {
        "menu_id": menu_id
    }

# 4. path parameter with post method

class Emp(BaseModel):
    name:str
    id:int

@app.post("/emp/{emp_id}")
def emp_code(emp:Emp,emp_id:int):
    return{
        "messege":"develop",
        "emp_id":emp
    }


@app.get("/Home")
def Hi():
    return{
        "messege":"Home is created"
    }

class Welcome(BaseModel):
    name:str
    location:str

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

class Welcome(BaseModel):
    name: str

@app.post("/step")
def student(welcome: Welcome):
    return {
        "message": "welcome button",
        "name": welcome.name
    }

# querry parameters 

# from fastapi import FastAPI

# app = FastAPI()


# Query parameter 
@app.get("/search")
def search(name: str, age: int):
    return {
        "name": name,
        "age": age
    }



@app.get("/start")
def Send(send_id:int,send_name:str):
    return{
        "send_id":send_id,
        "send_name":send_name
    }


# ✅ 2. Query Parameter With Default Value


@app.get("/student")
def student(name: str = "Unknown", age: int = 0):
    return {
        "name": name,
          "age": age
        }

# ✅ 4. Multiple Query Parameters

@app.get("/filter")
def filter_data(name:str,age:int,city:str):
    return{
        "name":name,
        "age":age,
        "city":city
    }

# 1. Basic Example (Path + Query)

@app.get("/student/{student_id}")
def student_details(student_id: int, name: str, city: str):
    return {
        "Student_id": student_id,
        "name": name,
        "city": city
    }


class Student1(BaseModel):
    name: str
    age: int
    city: str

@app.post("/student")
def create_student(student: Student1):
    return student



# put Method in fast api when we want update entire object 

class Student(BaseModel):
    name: str
    age: int
    city: str

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    return {
        "message": "Student Updated Successfully!",
        "id": student_id,
        "data": student
    }


class Company(BaseModel):
    name:str
    age:int
    location:str


@app.put("/company/{company_id}")
def update_company(company_id:int, company:Company):
    return{
        "messege": "update successfully",
        "id": company_id,
        "data":company
    }
