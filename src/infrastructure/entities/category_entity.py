from sqlalchemy import (
    MetaData, Table, Column, Integer, Text
)

metadata = MetaData()

CategoryEntity = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
)
