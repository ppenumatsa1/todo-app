import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler("todo_app.log", maxBytes=10485760, backupCount=5),
            logging.StreamHandler(),
        ],
    )


setup_logging()
