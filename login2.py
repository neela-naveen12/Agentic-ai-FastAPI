from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="user login")

# User model
class Login(BaseModel):
    email: str
    password: str

# Dummy user list
users = [
    {"email": "naveen@gmail.com", "password": "1234"},
    {"email": "test@example.com", "password": "abcd"},
    {"email": "user@gmail.com", "password": "pass123"}
]

@app.post("/login")
def login_user(user: Login):
    for u in users:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "Login Success!", "email": user.email}

    raise HTTPException(status_code=401, detail="Invalid email or password")
