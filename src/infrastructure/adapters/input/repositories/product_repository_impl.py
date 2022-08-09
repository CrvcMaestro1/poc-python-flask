from sqlalchemy import (
    create_engine, literal_column
)

from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product import Product
from src.infrastructure.entities.product_entity import ProductEntity


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> [Product]:
        pass
        # query = ProductEntity.select()
        # cursor = self.__connection.execute(query)
        # rows = cursor.fetchall()
        # return [Product(**row) for row in rows]

    def get(self, product_id: int) -> Product:
        pass
        # query = ProductEntity.select().where(ProductEntity.c.id == product_id)
        # cursor = self.__connection.execute(query)
        # row = cursor.fetchone()
        # return Product(**row)

    def create(self, product: Product) -> Product:
        pass
        # insert = ProductEntity.insert().values(**product.to_json()).returning(literal_column('*'))
        # cursor = self.__connection.execute(insert)
        # result = cursor.fetchone()
        # return Product(**result)

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
        # delete = (ProductEntity.delete().where(ProductEntity.c.id == product_id))
        # self.__connection.execute(delete)
