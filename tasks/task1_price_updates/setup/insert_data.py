import typing as t

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from logging_config import logger

from .models import PriceUpdate


def insert_data() -> None:
    db_url: str = "postgresql+psycopg2://dev_user:dev_password@localhost:5432/test_db"
    engine = create_engine(db_url)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    # Sample data to insert into the table
    data: t.List[t.Dict[str, t.Any]] = [
        {"product": "banana [single]", "date": "2020-01-21", "price": 1},
        {"product": "banana [single]", "date": "2020-01-22", "price": 2},
        {"product": "cheese", "date": "2020-01-23", "price": 1},
        {"product": "potatoes [pack]", "date": "2020-01-21", "price": 3},
        {"product": "potatoes [pack]", "date": "2020-01-30", "price": 3},
    ]

    # Insert or update data in the table
    for record in data:
        price_update: PriceUpdate = PriceUpdate(**record)
        session.merge(price_update)  # Use merge to update or insert
    session.commit()

    logger.info("Data inserted successfully!")


if __name__ == "__main__":
    insert_data()
