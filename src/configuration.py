import os

import inject
from flask import Flask

from src.domain.category.category_service_impl import CategoryServiceImpl
from src.domain.category.input.category_service import CategoryService
from src.domain.category.output.category_repository import CategoryRepository
from src.domain.product.output.product_repository import ProductRepository
from src.infrastructure.adapters.input.repositories.category_repository_impl import CategoryRepositoryImpl
from src.infrastructure.adapters.input.repositories.product_repository_impl import ProductRepositoryImpl


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(CategoryRepository, CategoryRepositoryImpl(application.config['DATABASE_URI']))
        binder.bind(ProductRepository, ProductRepositoryImpl(application.config['DATABASE_URI']))
        binder.bind(CategoryService, CategoryServiceImpl(CategoryRepositoryImpl(application.config['DATABASE_URI'])))

    inject.configure(config)


def configure_profiler(application: Flask) -> None:
    application.config["flask_profiler"] = {
        "enabled": application.config['DEBUG'],
        "storage": {
            "engine": "sqlalchemy",
            "db_url": application.config['DATABASE_URI']
        },
        "basicAuth": {
            "enabled": True,
            "username": "admin",
            "password": "admin"
        },
        "ignore": [
            "^/static/.*"
        ]
    }
