from sqlalchemy.orm import Session
from app.models.todo_models import Todo
from app.schemas.todo_schemas import TodoCreate, TodoUpdate, TodoResponse
from backend.app.core.todo_exceptions import TodoNotFoundException
from app.core.todo_logging import setup_logging
import logging
from typing import List, Optional


logger = logging.getLogger(__name__)


class TodoService:
    def __init__(self, model=Todo):
        self.model = model

    def create_todo(self, db: Session, todo: TodoCreate) -> TodoResponse:
        try:
            db_todo = self.model(**todo.dict())
            db.add(db_todo)
            db.commit()
            db.refresh(db_todo)
            logger.info(f"Todo created: {db_todo.id}")
            return TodoResponse.from_orm(db_todo)
        except Exception as e:
            logger.error(f"Error creating todo: {e}")
            db.rollback()
            raise

    def get_todo(self, db: Session, todo_id: int) -> TodoResponse:
        try:
            db_todo = db.query(self.model).filter(self.model.id == todo_id).first()
            if db_todo is None:
                logger.error(f"Todo not found: {todo_id}")
                raise TodoNotFoundException(todo_id)
            logger.info(f"Todo retrieved: {db_todo.id}")
            return TodoResponse.from_orm(db_todo)
        except Exception as e:
            logger.error(f"Error retrieving todo: {e}")
            raise

    def get_todos(
        self, db: Session, skip: int = 0, limit: int = 10
    ) -> List[TodoResponse]:
        try:
            db_todos = db.query(self.model).offset(skip).limit(limit).all()
            if not db_todos:
                logger.warning("No todos found")
            logger.info(f"Todos retrieved: {len(db_todos)} items")
            return [TodoResponse.from_orm(todo) for todo in db_todos]
        except Exception as e:
            logger.error(f"Error retrieving todos: {e}")
            raise

    def update_todo(self, db: Session, todo_id: int, todo: TodoUpdate) -> TodoResponse:
        try:
            db_todo = db.query(self.model).filter(self.model.id == todo_id).first()
            if db_todo is None:
                logger.error(f"Todo not found for update: {todo_id}")
                raise TodoNotFoundException(todo_id)
            for key, value in todo.dict(exclude_unset=True).items():
                setattr(db_todo, key, value)
            db.commit()
            logger.info(f"Todo updated: {db_todo.id}")
            return TodoResponse.from_orm(db_todo)
        except Exception as e:
            logger.error(f"Error updating todo: {e}")
            db.rollback()
            raise

    def delete_todo(self, db: Session, todo_id: int) -> None:
        try:
            db_todo = db.query(self.model).filter(self.model.id == todo_id).first()
            if db_todo is None:
                logger.error(f"Todo not found for deletion: {todo_id}")
                raise TodoNotFoundException(todo_id)
            db.delete(db_todo)
            db.commit()
            logger.info(f"Todo deleted: {todo_id}")
        except Exception as e:
            logger.error(f"Error deleting todo: {e}")
            db.rollback()
            raise
