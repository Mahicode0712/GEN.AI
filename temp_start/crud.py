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
 


def seed_db(db: Session):
    """Seed the database with sample products for search demonstrations."""
    # 1. Clear existing items from SQL and ChromaDB
    db.query(models.Item).delete()
    db.commit()
    
    global collection
    try:
        chroma_client.delete_collection(name="products")
    except Exception:
        pass
    collection = chroma_client.get_or_create_collection(name="products")
    
    # 2. Seed items
    seed_data = [
        {
            "name": "iPhone 15 Pro",
            "price": 120000,
            "description": "Flagship mobile phone with 5G connectivity, 120Hz OLED screen, and advanced triple-camera system.",
            "is_active": True
        },
        {
            "name": "Samsung Galaxy A14",
            "price": 15000,
            "description": "Budget-friendly cellular smartphone with long-lasting battery and dual SIM support.",
            "is_active": True
        },
        {
            "name": "MacBook Pro M3",
            "price": 170000,
            "description": "High-performance ultrabook laptop for software developers, featuring 32GB RAM and 1TB SSD.",
            "is_active": True
        },
        {
            "name": "Sony WH-1000XM5",
            "price": 30000,
            "description": "Over-ear wireless bluetooth headphones with active noise cancellation and high-fidelity sound.",
            "is_active": True
        },
        {
            "name": "Nike Air Zoom Running Shoes",
            "price": 8000,
            "description": "Comfortable running shoes designed for marathon runners with breathable mesh fabric.",
            "is_active": True
        },
        {
            "name": "Leather Wallet",
            "price": 1500,
            "description": "Genuine leather bi-fold wallet for men with RFID blocking card slots.",
            "is_active": True
        },
        {
            "name": "iPad Air",
            "price": 60000,
            "description": "Slim and powerful tablet with a liquid retina display, support for Apple Pencil, and cellular capabilities.",
            "is_active": True
        }
    ]
    
    seeded_items = []
    for item_dict in seed_data:
        item_schema = schemas.ItemCreate(**item_dict)
        db_item = create_item(db, item_schema)
        seeded_items.append(db_item)
        
    return seeded_items