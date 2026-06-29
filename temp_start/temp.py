from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def f():
    return  {"working":"success"}

@app.post(f"/post/{id}")   
def pfunc():
    return  {"user posted":f"id"}