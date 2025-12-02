
# ⭐ 1. Basic GET Example

# from fastapi import FastAPI

# app = FastAPI()


# @app.get('/hello')
# def say_hello():
#     return{'msg':"hello naveen"}


# ⭐ 2. GET With Path Parameter (value in URL)

# from fastapi import FastAPI
# myapp = FastAPI()

# @myapp.get("/user/{name}")
# def greet_user(name:str):
#     return {"messege":f"hello {name}"}


# 3. GET With Integer Path Parameter

# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/square/{num}")
# def square_number(num: int):
#     return {"square": num * num}

