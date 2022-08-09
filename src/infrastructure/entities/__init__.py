from sqlalchemy.ext.declarative import declarative_base

from src.infrastructure.entities.category_entity import CategoryEntity
from src.infrastructure.entities.product_entity import ProductEntity

Base = declarative_base()
metadata = [
    CategoryEntity.metadata,
    ProductEntity.metadata
]
