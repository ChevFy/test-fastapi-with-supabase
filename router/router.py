from fastapi import APIRouter , HTTPException , Depends
from typing import List
from sqlalchemy.orm import Session
import sys
sys.path.append("../")
from schema.schema import *
from models.models import *

router = APIRouter(prefix="/todos",tags=["todos"])

@router.get("/",response_model=List[TodoResponse])
def list_all_todos(db : Session = Depends(get_db)):
    return db.query(TodoDB).all()

@router.post("/")
def create_todo():
    pass
