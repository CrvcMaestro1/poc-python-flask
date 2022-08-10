from flask import jsonify

from src.domain.utils.exceptions import NotFound


def error_handler(f) -> object:
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            if isinstance(e, ValueError):
                return jsonify({'message': e.args[0], 'type': 'ValueError'}), 400
            elif isinstance(e, AttributeError):
                return jsonify({'message': e.args[0], 'type': 'AttributeError'}), 400
            elif isinstance(e, KeyError):
                return jsonify({'message': e.args[0], 'type': 'KeyError'}), 400
            elif isinstance(e, TypeError):
                return jsonify({'message': e.args[0], 'type': 'TypeError'}), 400
            elif isinstance(e, NotFound):
                return jsonify({'message': e.args[0], 'type': 'NotFound'}), 404
            else:
                return jsonify({'message': str(e), 'type': 'InternalServerError'}), 500

    wrapper.__name__ = f.__name__
    return wrapper
