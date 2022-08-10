from sqlalchemy import (
    create_engine, literal_column
)

from src.domain.category.category import Category
from src.domain.category.output.category_repository import CategoryRepository
from src.infrastructure.entities.category_entity import CategoryEntity


class CategoryRepositoryImpl(CategoryRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> [Category]:
        query = CategoryEntity.select()
        cursor = self.__connection.execute(query)
        rows = cursor.fetchall()
        return [Category(**row) for row in rows]

    def get(self, category_id: int) -> Category:
        query = CategoryEntity.select().where(CategoryEntity.c.id == category_id)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        return Category(**row)

    def create(self, category: Category) -> Category:
        insert = CategoryEntity.insert().values(**category.to_json()).returning(literal_column('*'))
        cursor = self.__connection.execute(insert)
        result = cursor.fetchone()
        return Category(**result)

    def update(self, category: Category) -> Category:
        update = (
            CategoryEntity.update().
            where(CategoryEntity.c.id == category.id).
            values(**category.to_json()).
            returning(literal_column('*'))
        )
        cursor = self.__connection.execute(update)
        result = cursor.fetchone()
        return Category(**result)

    def delete(self, category_id: int):
        delete = (CategoryEntity.delete().where(CategoryEntity.c.id == category_id))
        self.__connection.execute(delete)
