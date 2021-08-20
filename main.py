from fastapi import FastAPI
from fastapi.params import Query
from qldb.querying import *


app = FastAPI()

@app.get("/api/user_info")
async def read_root(
    Name: list = Query(Person_Name),
    Credit: list = Query(Credit_Number),
    Curr_Available: list = Query(Current_Available_Amount)):
    query_items = {"Name": Name,"Credit":Credit,"Curr_Available":Curr_Available}
    return query_items