from fastapi import FastAPI
from pymongo import MongoClient
import os

ATLAS_URL = os.environ["ATLAS_URL"]
DB_NAME = os.environ["DB_NAME"]

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(ATLAS_URL)
    app.database = app.mongodb_client[DB_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/test")
async def get_sales():
    sales = []
    for sale in app.database["sales"].find({}):
        sales.append(sale["customer"])
    
    return {"sales": sales}
