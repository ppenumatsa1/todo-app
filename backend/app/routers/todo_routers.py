from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.app.db.todo_dependencies import get_db
from app.schemas.todo_schemas import TodoCreate, TodoUpdate, TodoResponse
from app.services.todo_services import TodoService
from app.core.todo_logging import setup_logging
import logging

router = APIRouter()
todo_service = TodoService()
logger = logging.getLogger(__name__)


@router.post("/todos/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    try:
        result = todo_service.create_todo(db=db, todo=todo)
        logger.info(f"Todo created: {result.id}")
        return result
    except Exception as e:
        logger.error(f"Error creating todo: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/todos/", response_model=list[TodoResponse])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        result = todo_service.get_todos(db=db, skip=skip, limit=limit)
        logger.info(f"Todos retrieved: {len(result)} items")
        return result
    except Exception as e:
        logger.error(f"Error retrieving todos: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        todo = todo_service.get_todo(db=db, todo_id=todo_id)
        if todo is None:
            logger.error(f"Todo not found: {todo_id}")
            raise HTTPException(status_code=404, detail="Todo not found")
        logger.info(f"Todo retrieved: {todo.id}")
        return todo
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error retrieving todo: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    try:
        updated_todo = todo_service.update_todo(db=db, todo_id=todo_id, todo=todo)
        if updated_todo is None:
            logger.error(f"Todo not found for update: {todo_id}")
            raise HTTPException(status_code=404, detail="Todo not found")
        logger.info(f"Todo updated: {updated_todo.id}")
        return updated_todo
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error updating todo: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete("/todos/{todo_id}", response_model=None)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        todo_service.delete_todo(db=db, todo_id=todo_id)
        logger.info(f"Todo deleted: {todo_id}")
        return None
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error deleting todo: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
