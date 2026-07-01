from abc import update_abstractmethods
from sqlalchemy.orm import Session
import models, schemas


def create_item(db: Session, item:schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item); db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db, skip=0, limit=100):
    return db.query(models.Items).offset(skip).limit(limit).all()    


def get_item(db, item_id):
    return db.query(models.Item).filter(
        models.Item.id == item_id).first()

def update_item(db, item_id, updates):
    db_item = get_item(db, item_id)
    if not db_item: return None
    for f,v in updates.model_dump(exclude_unset = True).items():
        setattr(db_item,f,v)   # only updates sent files
    db_item.commit();db_item.refresh(db_item); return db_item   


def delete_item(db, item_id):
    db_item  = get_item(db, item_id)
    if not db_item:  return None
    db.delete(db_item); db.commit(); return db_item
 