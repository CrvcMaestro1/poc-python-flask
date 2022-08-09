from abc import (
    ABCMeta,
    abstractmethod
)

from src.tipti.domain.category.entities import Category


class CategoryManager:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list(self) -> [Category]:
        pass

    @abstractmethod
    def get(self, id: int) -> Category:
        pass

    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
