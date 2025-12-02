
from fastapi import FastAPI
import time
import asyncio

app = FastAPI()
@app.get("/sync")
def sync_api():
    return {"msg": "This is Sync API"}


@app.get("/async")
def async_api():
    return{
        "msg":"this is a async api"
    }


@app.get("/sync-slow")
def slow_sync():
    time.sleep(3)
    return{
        "msg":"sync-completed"
    }


@app.get("/async-slow")
async def slow_async():
    await asyncio.sleep(3)   # does NOT block
    return {"msg": "Async completed"}

@app.get("/async")
async def async_api():
    await asyncio.sleep(5)  # non-blocking
    return {"msg": "Async completed"}