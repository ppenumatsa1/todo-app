# TODO Application

This project is a TODO application that implements CRUD operations using a FastAPI backend and a React frontend. The application allows users to create, read, update, and delete TODO items.

## Project Structure


```
todo-app
├── .github
│   └── workflows
├── backend
│   ├── app
│   │   ├── core
│   │   │   ├── todo_logging.py
│   │   │   └── __init__.py
│   │   ├── db
│   │   │   ├── init_db.py
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── todo_models.py
│   │   │   └── __init__.py
│   │   ├── routers
│   │   │   ├── todo_routers.py
│   │   │   └── __init__.py
│   │   ├── schemas
│   │   │   ├── todo_schemas.py
│   │   │   └── __init__.py
│   │   ├── services
│   │   │   ├── todo_services.py
│   │   │   └ __init__.py
│   │   ├── exceptions
│   │   ├── main.py
│   │   └── todo_dependencies.py
│   ├── tests
├── frontend
│   ├── public
│   └── src
│       ├── components
│       └── services
│   ├── tests
├── infra
│   ├── bicep
│   └── kubernetes
├── scripts
│   ├── db
│   └── other_scripts
├── docs
└── README.md
```

## Backend

The backend is built using FastAPI and is organized into several modules:

- **Core**: Contains configuration and dependency management, including logging setup.
- **DB**: Handles database connections and interactions with PostgreSQL.
- **Models**: Defines data models using SQLAlchemy ORM.
- **Routers**: Contains route definitions for handling CRUD operations.
- **Schemas**: Defines Pydantic schemas for request and response validation.
- **Services**: Contains business logic for the application.

## Frontend

The frontend is built using React and is structured as follows:

- **Public**: Contains static assets such as images and the index.html file.
- **Src**: Contains React components and service functions for API calls.
- **Tests**: Contains unit tests for components and services.


## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/todo-app.git
    cd todo-app
    ```

2. Set up the PostgreSQL database and run the initialization script:
    ```sh
    psql -U your-username -f scripts/db/init.sql
    ```

3. Install the required dependencies for the backend:
    ```sh
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    export PYTHONPATH=./backend  # On Windows use `$env:PYTHONPATH = "./backend"`
    pip install -r requirements.txt
    ```

4. Run the backend server:
    ```sh
    uvicorn app.main:app --reload
    ```

5. Install the required dependencies for the frontend:
    ```sh
    cd ../frontend
    export NODE_OPTION=--openssl-legacy-provider  # On Windows use `$env:PYTHONPATH = "$env:NODE_OPTIONS="--openssl-legacy-provider""`
                            
    npm install
    ```

6. Run the frontend server:
    ```sh
    npm run build
    serve -s build
    ```

## Usage Guidelines

- Use the API endpoints defined in the backend to interact with TODO items.
- The frontend provides a user interface to manage TODO items.

## Testing

Unit tests are provided for both the backend and frontend. Run the tests to ensure the application functions as expected.

## Documentation

Refer to the `docs` folder for additional documentation related to the project.