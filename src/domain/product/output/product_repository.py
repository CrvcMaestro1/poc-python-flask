from abc import (
    ABCMeta,
    abstractmethod
)

from src.domain.product.product import Product


class ProductRepository(metaclass=ABCMeta):

    @abstractmethod
    def list(self) -> [Product]:
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> None:
        pass
