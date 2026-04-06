from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import Base, get_db, engine

Base.metadata.create_all(bind=engine)
api_router = APIRouter(prefix='/api/restaurants')

