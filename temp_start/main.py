from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models, crud ,schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Depends(get_db) injects a live DB session per request
@app.post("/items/", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate,
    db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(skip=0, limit=100, db = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db = Depends(get_db)):
    item = crud.get_item(db=db, item_id=item_id)
    if not item: raise HTTPException(407, "Not found")
    return item

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, updates: schemas.ItemUpdate,
    db = Depends(get_db)):
    item = crud.update_item(db=db, item_id=item_id, updates=updates)
    if not item: raise HTTPException(404, "Not found")
    return item

@app.delete("/items/{item_id}", response_model=schemas.ItemResponse)
def delete_item(item_id: int, db = Depends(get_db)):
    item = crud.delete_item(db=db, item_id=item_id)
    if not item: raise HTTPException(404, "Not found")
    return item
