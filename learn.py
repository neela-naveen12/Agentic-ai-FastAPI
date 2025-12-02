# from fastapi import FastAPI
# app = FastAPI()

# @app.get('/user')
# def welcome():
#     return{"data:{welcome to fastapi}"}



# Query parameter 

from fastapi import FastAPI

app = FastAPI()

# Simple query parameter
# URL example: http://127.0.0.1:8000/greet?name=Naveen
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


# example:2 =>sum of two numbers
from fastapi import FastAPI
app = FastAPI()

@app.get("/add")
def add_numbers(a: int, b:int):
    return{"result": a+b}


# example 3: even or odd 

from fastapi import FastAPI
app = FastAPI()


@app.get('/check')
def even_odd(num: int):
    return{"result": num, "even": num%2==0}


