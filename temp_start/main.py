from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models, crud ,schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post(f"/post/{id}")   
def pfunc():
    return  {"user posted":f"id"}