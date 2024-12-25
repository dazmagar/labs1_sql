import typing as t

from sqlalchemy import create_engine

from logging_config import logger

from .models import Base


def create_tables() -> None:
    db_url: str = "postgresql+psycopg2://dev_user:dev_password@localhost:5432/test_db"
    engine = create_engine(db_url)

    # Create all tables defined in models.py
    Base.metadata.create_all(engine)
    logger.info("Tables created successfully!")


if __name__ == "__main__":
    create_tables()
