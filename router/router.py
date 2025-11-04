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

@router.post("/", response_model=TodoResponse)
def create_todo(todo : TodoCreate , db : Session = Depends(get_db)):
    db_todo = TodoDB(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{id}")
def delete_todo_by_id(id : int , db : Session = Depends(get_db)):
    db_todo = db.query(TodoDB).filter(TodoDB.id ==  id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_todo)
    db.commit()
    return { "todo was deleted"}

    
