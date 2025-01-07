class TodoNotFoundException(Exception):
    def __init__(self, todo_id: int):
        self.todo_id = todo_id
        super().__init__(f"Todo with id {todo_id} not found")


class TodoAlreadyExistsException(Exception):
    def __init__(self, todo_title: str):
        self.todo_title = todo_title
        self.message = f"Todo with title '{self.todo_title}' already exists."
        super().__init__(self.message)


class InvalidTodoDataException(Exception):
    def __init__(self, errors: dict):
        self.errors = errors
        self.message = "Invalid data provided for Todo."
        super().__init__(self.message)


class DatabaseConnectionException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
