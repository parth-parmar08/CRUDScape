from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware

from routers.create import router as item_router
from routers.read import router as read_router

app = FastAPI()

app.include_router(item_router, prefix="/create", tags=["items"])
app.include_router(read_router, prefix="/read", tags=["items"])