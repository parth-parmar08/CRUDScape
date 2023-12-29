from fastapi import APIRouter, HTTPException, Depends
#from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
#from pydantic.fields import Annotated
import models
from database import engine
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()
# MongoDB connection URL
#MONGO_URL = "mongodb://localhost:27017"
#client = AsyncIOMotorClient(MONGO_URL)
#database = client["mydb"]
#collection = database["items"]


#Create our Tables in Postgres
models.Base.metadata.create_all(bind=engine)

class Items(BaseModel):
    name: str
    description: str 


#Connecting to out Postgres Server
def get_db_dependency(db: Session = Depends(get_db)):
    return db

#item_id = item.id

@router.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db_dependency)):
    result = db.query(models.Items).filter(models.Items.id == item_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Item not found')
    return result
