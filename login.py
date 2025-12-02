from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    email: str
    password: str

dummy_user = {
    "email": "test@example.com",
    "password": "12345"
}

@app.post("/login")
def login_user(user: Login):
    if user.email == dummy_user["email"] and user.password == dummy_user["password"]:
        return {"message": "Login Successful"}

    raise HTTPException(status_code=401, detail="Invalid email or password")
