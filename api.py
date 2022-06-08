from fastapi import FastAPI, Header
from typing import Optional

import psutil, requests

app = FastAPI()


@app.get("/hello")
async def root(x_oblv_user_name: Optional[str] = Header(None)):
    return {"message": "Hello " + x_oblv_user_name}

@app.get("/resources")
async def resources(x_oblv_user_name: Optional[str] = Header(None)):
    return {
        "CPU %": psutil.cpu_percent(interval=1, percpu=True),
        "Virtual Memory:": psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        }

@app.get("/select_model")
async def select_model(model_meta, x_oblv_user_name: Optional[str] = Header(None)):
    return {"model_meta": model_meta}


@app.get("/rest_in")
async def rest_in(x_oblv_user_name: Optional[str] = Header(None)):
    print("endpoint called")
    r = requests.get(url = "http://reqres.in/api/users", params = {"page": 2})
    print("endpoint finish")
    print(str(r))
    return r.json()