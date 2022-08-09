import inject

from src.domain.product.input.product_service import ProductService
from src.domain.product.output.product_repository import ProductRepository
from src.domain.product.product import Product


class ProductServiceImpl(ProductService):

    @inject.autoparams()
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def list(self) -> [Product]:
        return self.repository.list()

    def get(self, product_id: int) -> Product:
        return self.repository.get(product_id)

    def create(self, product: Product) -> Product:
        return self.repository.create(product)

    def update(self, product: Product) -> Product:
        return self.repository.update(product)

    def delete(self, product_id: int) -> None:
        self.repository.delete(product_id)
