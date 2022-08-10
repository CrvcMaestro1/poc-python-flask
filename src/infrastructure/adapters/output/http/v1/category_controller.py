import inject
from flask import Blueprint, jsonify, Response, request
from src.domain.category.category import Category
from src.domain.category.input.category_service import CategoryService
from src.infrastructure.adapters.output.http.utils.error_handler import error_handler


@inject.autoparams()
def category_blueprint(
        category_service: CategoryService
) -> Blueprint:
    blueprint = Blueprint('category', __name__)

    @blueprint.route('/categories')
    @error_handler
    def categories_list() -> Response:
        categories = category_service.list()
        return jsonify({
            'results': [category.to_dict() for category in categories]
        })

    @blueprint.route('/categories/<int:category_id>')
    @error_handler
    def category_get(category_id: int) -> Response:
        category = category_service.get(category_id)
        return jsonify(category.to_dict())

    @blueprint.route('/categories', methods=['POST'])
    @error_handler
    def category_create() -> Response:
        data: dict | None = request.get_json()
        category_object = Category.from_dict_to_dataclass(data)
        category = category_service.create(category_object)
        return jsonify(category.to_dict())

    @blueprint.route('/categories/<int:category_id>', methods=['PUT'])
    @error_handler
    def category_update(category_id: int) -> Response:
        data: dict | None = request.get_json()
        data["id"] = category_id
        category_object = Category.from_dict_to_dataclass(data)
        category = category_service.update(category_object)
        return jsonify(category.to_dict())

    return blueprint
