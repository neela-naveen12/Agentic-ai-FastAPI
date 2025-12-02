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

@app.post("/post")
def post_data():
    return "hello"


class User(BaseModel):
    name: str
    age: int

# POST endpoint
@app.post("/create_user")
def create_user(user: User):
    return {"message": f"User {user.name} of age {user.age} created successfully!"}



class Details(BaseModel):
    name: str
    age: int
    location: str
    phno:int

@app.post('/user')
def user_details(details:Details):
    return{"messege":f"{details.name} at age of {details.age}from {details.location}"}


class Product(BaseModel):
    name :str
    price:float
    in_stock :bool = True

@app.post('/product')
def product_details(product:Product):
    return Product

