from sqlalchemy import (
    MetaData, Table, Column, Integer, Text, Numeric, Boolean, ForeignKey
)

metadata = MetaData()

ProductEntity = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
    Column('stock', Numeric, nullable=False),
    Column('price', Numeric, nullable=False),
    Column('pvp', Numeric, nullable=False),
    Column('has_discount', Boolean, nullable=False),
    Column('category_id', Integer, ForeignKey("categories.id"), nullable=False),
)
