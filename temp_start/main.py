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

@app.get("/items/filter")
def filter_items(min_price: int = None, max_price: int = None,db = Depends(get_db)):
    items = crud.get_item_by_price(db=db, min_price=min_price, max_price=max_price)
    if not items: raise HTTPException(404, "No items found")
    return items

@app.get("/items/search")
def search_items(keyword: str = None,min_price: int = None,max_price: int = None,skip: int = 0,limit: int = 100,db: Session = Depends(get_db)):
    results = crud.search_items(db=db,keyword=keyword,min_price=min_price,max_price=max_price,skip=skip,limit=limit)
    if not results:raise HTTPException(404, "No items found")
    
    return {
        "total": len(results),
        "filters": {
            "keyword": keyword,
            "min_price": min_price,
            "max_price": max_price
        },
        "items": results
    }

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

@app.post("/items/seed", response_model=list[schemas.ItemResponse])
def seed_database(db: Session = Depends(get_db)):
    return crud.seed_db(db=db)
