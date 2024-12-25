from sqlalchemy import Column, Date, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()


# Define the price_updates table
class PriceUpdate(Base):
    __tablename__ = "price_updates"

    product: str = Column(String(255), nullable=False, primary_key=True)
    date: Date = Column(Date, nullable=False, primary_key=True)
    price: int = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint("product", "date", name="unique_product_date"),)
