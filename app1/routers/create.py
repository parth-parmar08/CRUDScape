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

#db_dependency = Annotated[Session, Depends(get_db)]

#Create Item
@router.post("/items/")
async def create_item(item: Items, db: Session = Depends(get_db_dependency)):
    result = models.Items(name=item.name,description=item.description)
    #r2 = models.Items(description=item.description)
    db.add(result)
    db.commit()
    db.refresh(result)
    #item.id = str(result.inserted_id)
    return result


#@router.get("/items/{name}", response_model=Item)
#async def read_item(name: str):
#    item = await collection.find_one({"_id": item_id})
#    if item:
#        return item
#    raise HTTPException(status_code=404, detail="Item not found")