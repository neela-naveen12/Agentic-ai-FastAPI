
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from typing import Optional

# logging setup 

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(messege)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Bank Account API")

accounts ={}

# pydantic models 

class createbankaccount(BaseModel):
    id:int
    name:str
    initial_amount: float = 0.0


class fundamount(BaseModel):
    id:int
    amount:float

# create account 
@app.post("/create_account")
async def create_account(data:createbankaccount):
    logger.info(f"bank account is created:{data.id}")
    if data.id  in accounts:
        logger.warning(f"bank account is already exist:{data.id}")
        raise HTTPException(status_code=404,detail="already exist")
    
    accounts[data.id] = data.initial_amount
    return{
        "messege":f"bank account is created:{data.id}",
        "id":data.id,
        "name":data.name
    }
# get bank details 

@app.get("/accounts/{account_id}")
async def bank_details(account_id:int):
    if account_id not in accounts:
        logger.warning(f"account not exist:{account_id}")
        raise HTTPException(status_code=404,detail="not exist")
    return {
        "messege":"account trieve",
        "account" :accounts[account_id]
    }

# fund amount 

@app.post("/account")
async def fund_amount(data:fundamount):
    if data.id not in accounts:
        logger.warning(f"not found:{data.id}")
        raise HTTPException(status_code=404,detail="not found")
    
    accounts[data.id] += data.amount
    return{
        "messege":"amount added sucessfully!",
        "id":data.id,
        "total-amount":accounts[data.id]
    }

# withdraw amount 

@app.post("/account_withdraw")
async def withdraw_amount(data:fundamount):
    if data.id not in accounts:
        logger.info(f"bank doesnot exist:{data.id}")
        raise HTTPException(status_code=404, detail="not found")
    accounts[data.id] -= data.amount
    return{
        "messege":"amount withdraw sucessfull!",
        "id":data.id,
        "balance":accounts[data.id]
    }

# delete account 
@app.delete("/delete/{account_id}")
async def delete_account(account_id:int):
    if account_id not in accounts:
        raise HTTPException(status_code=404,detail="not found")
    
    delete_account = accounts.pop(account_id)
    return{
        "messege":"account deleted sucessfully!",
        "delete":delete_account
    }
    