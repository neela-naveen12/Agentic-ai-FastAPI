from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    email: str
    password: str

users_db = []   # Empty list

@app.post("/signup")
def signup(user: User):
    for u in users_db:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    users_db.append(user.dict())
    return {"message": "Signup successful!"}

@app.post("/login")
def login(user: User):
    for u in users_db:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "Login successful!"}

    raise HTTPException(status_code=401, detail="Invalid credentials")
