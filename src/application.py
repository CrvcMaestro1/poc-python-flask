from flask import Flask
import flask_profiler
from src.configuration import configure_inject, configure_application, configure_profiler

from src.infrastructure.adapters.output.http.v1.category_controller import category_blueprint
from src.infrastructure.adapters.output.http.v1.product_controller import product_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    configure_application(application)
    configure_inject(application)
    configure_profiler(application)

    application.register_blueprint(category_blueprint(), url_prefix='/api')
    application.register_blueprint(product_blueprint(), url_prefix='/api')

    # flask_profiler.init_app(application)

    return application
