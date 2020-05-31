import logging

from flask import Flask

from api.routes import base_blueprint


# Config variables that can be overridden with envvars
CUSTOM_CONFIG = {
    'BRAINTREE_MERCHANT_ID': 'dummy',
    'BRAINTREE_PUBLIC_KEY': 'dummy',
    'BRAINTREE_PRIVATE_KEY': 'dummy',
    'ENVIRONMENT': 'sandbox',  # for prod use: 'production' 
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
