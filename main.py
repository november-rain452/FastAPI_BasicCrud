from fastapi import FastAPI
from routes.router import api_router
import models
from core.database import engine,Base

app = FastAPI()
app.include_router(api_router)
Base.metadata.create_all(bind=engine)