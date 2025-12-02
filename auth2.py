
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class Mobile(BaseModel):
    phone: str

@app.post("/send-otp")
def send_otp(data: Mobile):
    otp = random.randint(1000, 9999)
    return {"message": "OTP sent successfully", "otp": otp}
