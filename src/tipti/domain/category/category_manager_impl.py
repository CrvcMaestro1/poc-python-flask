from src.tipti.domain.category.category_manager import CategoryManager
from src.tipti.domain.category.entities import Category
from src.tipti.infrastructure.category.repository import CategoryRepository


class CategoryManagerImpl(CategoryManager):

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def list(self) -> [Category]:
        return self.repository.list()

    def get(self, id: int) -> Category:
        return  self.repository.get(id)

    def create(self, category: Category) -> Category:
        return self.repository.create(category)

    def update(self, category: Category) -> Category:
        return self.repository.update(category)

    def delete(self, id: int) -> None:
        self.repository.delete(id)
