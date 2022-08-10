import inject
from flask import Blueprint, jsonify, Response, request

from src.domain.product.input.product_service import ProductService
from src.domain.product.product import Product
from src.infrastructure.adapters.output.http.utils.error_handler import error_handler


@inject.autoparams()
def product_blueprint(
        product_service: ProductService
) -> Blueprint:
    blueprint = Blueprint('product', __name__)

    @blueprint.route('/products')
    @error_handler
    def product_list() -> Response:
        products = product_service.list()
        return jsonify({
            'results': [product.to_dict() for product in products]
        })

    @blueprint.route('/products/<int:product_id>')
    @error_handler
    def product_get(product_id: int) -> Response:
        product = product_service.get(product_id)
        return jsonify(product.to_dict())

    @blueprint.route('/products', methods=['POST'])
    @error_handler
    def product_create() -> Response:
        data: dict | None = request.get_json()
        product_object = Product.from_dict_to_dataclass(data)
        product = product_service.create(product_object)
        return jsonify(product.to_json_pure())

    @blueprint.route('/products/<int:product_id>', methods=['PUT'])
    @error_handler
    def product_update(product_id: int) -> Response:
        data: dict | None = request.get_json()
        data["id"] = product_id
        product_object = Product.from_dict_to_dataclass(data)
        product = product_service.update(product_object)
        return jsonify(product.to_json_pure())

    return blueprint
