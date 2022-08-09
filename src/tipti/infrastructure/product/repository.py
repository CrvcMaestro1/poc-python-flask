from abc import (
    ABCMeta,
    abstractmethod
)

from src.tipti.domain.product.entities import Product


class ProductRepository(metaclass=ABCMeta):

    @abstractmethod
    def list(self) -> [Product]:
        pass

    @abstractmethod
    def get(self, id: int) -> Product:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
