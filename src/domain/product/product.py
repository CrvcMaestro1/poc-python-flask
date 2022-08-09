from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from src.domain.category.category import Category


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Product:
    id: int
    name: str
    stock: float
    price: float
    pvp: float
    has_discount: bool
    category: Category
