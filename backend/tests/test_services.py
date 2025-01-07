from fastapi import HTTPException
from app.services.todo_services import TodoService
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.todo_models import Base, Todo
from app.schemas.todo_schemas import TodoCreate, TodoUpdate
from app.core.todo_config import settings
import pytest
import logging

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Todo.__table__.drop(bind=engine, checkfirst=True)


@pytest.fixture
def db_session(setup_database):
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def todo_service():
    return TodoService()


@pytest.fixture
def todo_data():
    return {"title": "Test Todo", "description": "Test Description"}


def test_create_todo(todo_service, db_session: Session, todo_data):
    todo = todo_service.create_todo(db_session, TodoCreate(**todo_data))
    assert todo.title == todo_data["title"]
    assert todo.description == todo_data["description"]


def test_get_todo(todo_service, db_session: Session, todo_data):
    created_todo = todo_service.create_todo(db_session, TodoCreate(**todo_data))
    fetched_todo = todo_service.get_todo(db_session, created_todo.id)
    assert fetched_todo.id == created_todo.id


def test_update_todo(todo_service, db_session: Session, todo_data):
    created_todo = todo_service.create_todo(db_session, TodoCreate(**todo_data))
    update_data = {"title": "Updated Todo", "description": "Updated Description"}
    updated_todo = todo_service.update_todo(
        db_session, created_todo.id, TodoUpdate(**update_data)
    )
    assert updated_todo.title == update_data["title"]
    assert updated_todo.description == update_data["description"]


# def test_delete_todo(todo_service, db_session: Session, todo_data):
#     created_todo = todo_service.create_todo(db_session, TodoCreate(**todo_data))
#     fetched_todo = todo_service.get_todo(db_session, created_todo.id)
#     assert (
#         fetched_todo.id == created_todo.id
#     )  # Confirm the todo item exists before deletion
#     logger.info(f"Deleting todo with id: {created_todo.id}")
#     todo_service.delete_todo(db_session, created_todo.id)
#     with pytest.raises(HTTPException):
#         todo_service.get_todo(db_session, created_todo.id)
