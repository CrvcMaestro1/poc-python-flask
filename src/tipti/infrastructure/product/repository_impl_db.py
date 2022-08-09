from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, literal_column, Numeric, Boolean, ForeignKey
)

from src.tipti.domain.product.entities import Product
from src.tipti.infrastructure.category.repository_impl_db import categories
from src.tipti.infrastructure.product.repository import ProductRepository

metadata = MetaData()

products = Table(
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


class ProductRepositoryImplDb(ProductRepository):

    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def list(self) -> [Product]:
        # [
        #                 products.c.id,
        #                 products.c.name
        #              ]

        # query = (products.select().columns([products.c.id, products.c.name, products.c.category_id]))
        query = (products.select().join(categories, categories.id == products.id))

        cursor = self.__connection.execute(query)
        rows = cursor.fetchall()
        return [Product(**row) for row in rows]

    def get(self, id: int) -> Product:
        query = products.select().where(products.c.id == id)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        return Product(**row)

    def create(self, product: Product) -> Product:
        insert = products.insert().values(**product.to_json()).returning(literal_column('*'))
        cursor = self.__connection.execute(insert)
        result = cursor.fetchone()
        return Product(**result)

    def update(self, product: Product) -> Product:
        update = (
            products.update()
            .where(products.c.id == product.id)
            .values(**product.to_json())
            .returning(literal_column('*'))
        )
        cursor = self.__connection.execute(update)
        result = cursor.fetchone()
        return Product(**result)

    def delete(self, id: int):
        delete = (products.delete().where(products.c.id == id))
        self.__connection.execute(delete)
