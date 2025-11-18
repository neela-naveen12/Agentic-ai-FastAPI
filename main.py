
from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def home():
    return {'data':{'this is a home Page'}}


@app.get('/about')
def about():
    return {'data':{'this is a about page'}}