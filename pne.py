
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {}

class student(BaseModel):
    id:int
    name:str
    age :int


@app.post("/add_student")
async def add_student(st:student):
    if st.id in students:
        raise HTTPException(status_code=400,detail="student already exist")
    
    students[st.id] = st.dict()
    return students[st.id]




products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 900}
]

@app.get("/filter")
def filter_price(max_price: int):
    return [p for p in products if p["price"] <= max_price]
