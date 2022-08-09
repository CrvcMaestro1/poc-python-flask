import inject
from src.domain.category.input.category_service import CategoryService
from src.domain.category.category import Category
from src.domain.category.output.category_repository import CategoryRepository


class CategoryServiceImpl(CategoryService):

    @inject.autoparams()
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def list(self) -> [Category]:
        return self.repository.list()

    def get(self, category_id: int) -> Category:
        return self.repository.get(category_id)

    def create(self, category: Category) -> Category:
        return self.repository.create(category)

    def update(self, category: Category) -> Category:
        return self.repository.update(category)

    def delete(self, category_id: int) -> None:
        self.repository.delete(category_id)
