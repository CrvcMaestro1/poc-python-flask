from src.tipti.domain.category.entities import Category
from src.tipti.infrastructure.category.repository import CategoryRepository

from typing import Optional, List

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, func, select, literal_column
)

metadata = MetaData()

categories = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
)


class CategoryRepositoryImplDb(CategoryRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> [Category]:
        query = categories.select()
        cursor = self.__connection.execute(query)
        rows = cursor.fetchall()
        return [Category(**row) for row in rows]

    def get(self, id: int) -> Category:
        query = categories.select().where(categories.c.id == id)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        return Category(**row)

    def create(self, category: Category) -> Category:
        insert = categories.insert().values(**category.to_json()).returning(literal_column('*'))
        cursor = self.__connection.execute(insert)
        result = cursor.fetchone()
        return Category(**result)

    def update(self, category: Category) -> Category:
        update = (
            categories.update()
            .where(categories.c.id == category.id)
            .values(**category.to_json())
            .returning(literal_column('*'))
        )
        cursor = self.__connection.execute(update)
        result = cursor.fetchone()
        return Category(**result)

    def delete(self, id: int):
        delete = (categories.delete().where(categories.c.id == id))
        self.__connection.execute(delete)
