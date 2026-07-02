from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name:str; description: Optional[str] = None
    price:int; is_active: bool = True

class ItemCreate(ItemBase): pass

# PUT body --  every field
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    is_active: Optional[bool] = None

#response -- adds id, read ORM objects directly
class ItemResponse(ItemBase):
    id:int
    class Config:
        from_atrribute = True    #pydantic  v2 

#RAG recommendation response
class RAGRecommendationResponse(BaseModel):
    query: str
    retrieved_items: list[ItemResponse]
    prompt_sent: str
    recommendation: str