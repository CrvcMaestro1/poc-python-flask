from sqlalchemy import (
    create_engine, literal_column, select
)

from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product import Product
from src.infrastructure.entities import CategoryEntity
from src.infrastructure.entities.product_entity import ProductEntity


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> [Product]:
        query = select(
            [
                ProductEntity,
                CategoryEntity.c.name.label('category_name')
            ]
        ).where(ProductEntity.c.category_id == CategoryEntity.c.id)
        cursor = self.__connection.execute(query)
        rows = cursor.fetchall()
        return [Product.from_dict_to_dataclass(row._mapping) for row in rows]

    def get(self, product_id: int) -> Product:
        query = select(
            [
                ProductEntity,
                CategoryEntity.c.name.label('category_name')
            ]
        ).where(ProductEntity.c.category_id == CategoryEntity.c.id). \
            filter(ProductEntity.c.id == product_id)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        return Product.from_dict_to_dataclass(row._mapping)

    def create(self, product: Product) -> Product:
        insert = ProductEntity.insert() \
            .values(**product.to_create()) \
            .returning(ProductEntity, CategoryEntity.c.name.label('category_name'))
        cursor = self.__connection.execute(insert)
        result = cursor.fetchone()
        return Product(**result)

    def update(self, product: Product) -> Product:
        pass
        # update = (
        #     ProductEntity.update()
        #         .where(ProductEntity.c.id == product.id)
        #         .values(**product.to_json())
        #         .returning(literal_column('*'))
        # )
        # cursor = self.__connection.execute(update)
        # result = cursor.fetchone()
        # return Product(**result)

    def delete(self, product_id: int):
        pass
