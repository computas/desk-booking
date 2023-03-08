from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URL"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"msg": "Hellosdadas World"}

@app.get("/test")
async def get_sales():
    sales = []
    for sale in app.database["sales"].find({}):
        print(sale)
    
    # Return the retrieved documents as a JSON response
    return {"sales": sales}
