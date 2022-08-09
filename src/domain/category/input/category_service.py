from abc import (
    ABCMeta,
    abstractmethod
)

from src.domain.category.category import Category


class CategoryService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def list(self) -> [Category]:
        pass

    @abstractmethod
    def get(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass
