"""
Simple Flask API to interact with the data.
"""

import logging

from flask import Flask

from tokenpay.routes import base_blueprint


# config defaults that can be overridden with envvars
CUSTOM_CONFIG = {
}


def create_app(user_config: dict) -> Flask:
    logging.basicConfig(level=logging.DEBUG)

    app = Flask(__name__)

    custom_config = {
        key: user_config.get(key, default_value)
        for key, default_value in CUSTOM_CONFIG.items()
    }
    app.config.update(custom_config)

    app.register_blueprint(base_blueprint)

    return app
