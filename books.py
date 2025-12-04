from fastapi import FastAPI,HTTPException

app = FastAPI()
books = [
    {
        "id":1,
        "title": "Python Programming",
        "author": "John Doe",
        "price": 499
    }
]

@app.post("/books")
def add_book(book:dict):
    book["id"] = len(books)+1
    books.append(book)
    return book

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/{book_id}")
def get_book_by_id(book_id:int):
    for bk in books:
        if bk["id"] == book_id:
            return bk
    raise HTTPException(status_code=404,detail="book not found")

@app.put("/books/{book_id}")
def update_book(book_id:int, updated:dict):
    for i,b in enumerate(books):
        if b["id"] == book_id:
            update_book["id"] = book_id
            books[i] = updated
            return updated
        
    raise HTTPException(status_code=404,detail="book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            return{
                "messege":"book deleted"
            }
    raise HTTPException(status_code=400,detail="book not found")


# ✅ 2. Store & Retrieve Messages (POST + GET)

messeges = []
@app.post("/messege")
def add_msg(msg:dict):
    messeges.append(msg)
    return msg

@app.get("/messege")
def get_msg():
    return messeges


# ✅ 3. Add Two Numbers (POST)

@app.post("/add")
def add_numbers(data:dict):
    return{
        "sum":data["a"] + data["b"]
    }

Students =[
     {"id": 1, "name": "Naveen"},
    {"id": 2, "name": "Ravi"},
    {"id": 3, "name": "Kiran"}
    
]

@app.get("/search")
def get_by_name(name:str):
    for s in Students:
        if s["name"].lower == name.lower():
            return s
    raise HTTPException(status_code=4004,detail="not found")



products = [
    {"id": 1, "name": "Phone", "price": 10000},
    {"id": 2, "name": "Laptop", "price": 50000}
]

@app.get("/products")
def get_product(max_price:int):
    return [p for p in products if p["price"]<=max_price]
    raise HTTPException(status_code=404,detail="product not found")

