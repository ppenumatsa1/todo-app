from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.models.todo_models import Base
from app.core.todo_config import settings
import os
import logging
import psycopg2
from psycopg2 import sql
from app.core.todo_logging import setup_logging

setup_logging()

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)


def create_database_if_not_exists(conn, database_name):
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(
        sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [database_name]
    )
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(
            sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name))
        )
        logger.info(f"Database '{database_name}' created successfully")
    cursor.close()


def create_schema_if_not_exists(conn, schema_name):
    cursor = conn.cursor()
    cursor.execute(
        sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema_name))
    )
    logger.info(f"Schema '{schema_name}' created successfully")
    cursor.close()


def init_db():
    try:
        # Read the init.sql file
        init_sql_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../scripts/db/init.sql")
        )
        with open(init_sql_path, "r") as file:
            init_script = file.read()

        logger.info(f"Executing SQL script from: {init_sql_path}")

        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default database
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
        )

        logger.info("Connected to PostgreSQL server")

        # Create the database if it does not exist
        database_name = settings.DATABASE_NAME
        create_database_if_not_exists(conn, database_name)

        # Close the connection to the default database
        conn.close()

        # Connect to the newly created database
        conn = psycopg2.connect(
            dbname=database_name,  # Connect to the newly created database
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            host=settings.DATABASE_HOST,
            port=settings.DATABASE_PORT,
        )
        conn.autocommit = True

        logger.info("Connected to the newly created database")

        # Create the schema if it does not exist
        create_schema_if_not_exists(conn, "todo")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the init.sql script to create schema and tables
        cursor.execute(sql.SQL(init_script))

        logger.info("Schema and tables creation script executed successfully")

        # Close the cursor and connection
        cursor.close()
        conn.close()

        logger.info("Database initialized successfully")
    except psycopg2.Error as e:
        logger.error(f"Error initializing database: {e}")
    except FileNotFoundError as e:
        logger.error(f"SQL script file not found: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
