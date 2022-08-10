from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=False)
class Category:
    id: int | None
    name: str

    @staticmethod
    def from_dict_to_dataclass(data):
        return Category(
            id=data.get('id'),
            name=data.get('name')
        )

    def to_create(self):
        return {
            "name": self.name
        }

    def to_update(self):
        return {
            "name": self.name
        }
