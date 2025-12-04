
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()


# accounts ={}    

# class createbankaccount(BaseModel):
#     id:int
#     name:str
#     intial_amount:float


# class fundamount(BaseModel):
#     id:int
#     amount:float


# # create account 

# @app.post("/create_account")
# async def create_new_account(data:createbankaccount):
#     if data.id in accounts:
#         raise HTTPException(status_code=404,detail="acount already exist")
    
#     accounts[data.id] = data.intial_amount

#     return{
#         "messege":"account created successfully",
#         "id":data.id,
#         "name":data.name,
#         "balance":accounts[data.id]


#     }

# # add fund 

# @app.post("/fund")
# async def add_fund(data:fundamount):
#     if data.id not in accounts:
#         raise HTTPException(status_code=400,detail="not found user")
    
#     accounts[data.id] += data.amount

#     return{
#         "messege":"fund added sucessfully",
#         "id":data.id,
#         "current_balance":accounts[data.id]
#     }

# @app.post("/withdraw")
# async def amount_withdraw(data: fundamount):

#     if data.id not in accounts:
#         raise HTTPException(status_code=404, detail="Account not found")

#     if accounts[data.id] < data.amount:
#         raise HTTPException(status_code=400, detail="Insufficient balance")

#     accounts[data.id] -= data.amount

#     return {
#         "message": "Amount withdrawn successfully!",
#         "id": data.id,
#         "remaining_amount": accounts[data.id]
#     }

# # with logging 

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import logging

# logging configuration 

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(messege)s"
)

logger = logging.getLogger("bank")


app = FastAPI()

accounts = {}

class createbankaccount(BaseModel):
    id:int
    name:str
    intial_amount:float

class fundamount(BaseModel):
    id:int
    amount:float

# create a bank account 
@app.post("/create_account")
async def create_new_account(data: createbankaccount):

    logger.info(f"Creating account for ID: {data.id}")   # LOG

    if data.id in accounts:
        logger.warning(f"Account already exists: {data.id}")   # LOG
        raise HTTPException(status_code=404, detail="account already exists")

    accounts[data.id] = data.intial_amount

    logger.info(f"Account created successfully: {data.id}")     # LOG

    return {
        "message": "Account created successfully",
        "id": data.id,
        "name": data.name,
        "balance": accounts[data.id]
    }


# add fund 

@app.post("/add_fund")
async def depo_fund(data:fundamount):
    logger.info(f"amount to be add {data.id}")

    if data.id not in accounts:
        logger.warning(f"their is no account{data.id}")
        raise HTTPException(status_code=400,detail="account not found")
    
    accounts[data.id]+= data.amount

    logger.info(f"amount added sucessfully{data.id}")

    return{
        "messege":"fund added sucessfully",
        "id":data.id,
        "total_amount": accounts[data.id]
    }

# withdraw fund 

@app.post("/withdraw_fund")
async def withdraw_amount(data:fundamount):
    logger.info(f"user want to withdraw amount:{data.id}")

    if data.id not in accounts:
        logger.error(f"account not exist:{data.id}")
        raise HTTPException(status_code=404,detail="not found")
    
    if accounts[data.id]<data.amount:
        logger.warning(f"insufficient fund:{data.id}")
        raise HTTPException(status_code=404,detail="insufficient fund")
    
    accounts[data.id]-=data.amount

    logging.info(f"amount withdrawn:{data.amount}from id{data.id}")

    return{
        "messege":"amount withdrwan sucessfully",
        "id":data.id
    }

