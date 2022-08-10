from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from src.domain.category.category import Category


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass(frozen=False)
class Product:
    id: int
    name: str
    stock: float
    price: float
    pvp: float
    has_discount: bool
    category: Category

    @staticmethod
    def from_dict_to_dataclass(data):
        return Product(
            id=data.get('id'),
            name=data.get('name'),
            stock=data.get('stock'),
            price=data.get('price'),
            pvp=data.get('pvp'),
            has_discount=data.get('has_discount'),
            category=Category(
                id=data.get('category_id'),
                name=data.get('category_name')
            )
        )

    def to_create(self):
        return {
            "name": self.name,
            "stock": self.stock,
            "price": self.price,
            "pvp": self.pvp,
            "has_discount": self.has_discount,
            "category_id": self.category.id
        }

    def to_update(self):
        return {
            "name": self.name,
            "stock": self.stock,
            "price": self.price,
            "pvp": self.pvp,
            "has_discount": self.has_discount,
            "category_id": self.category.id
        }

    def to_json_pure(self):
        return {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "price": self.price,
            "pvp": self.pvp,
            "has_discount": self.has_discount
        }
