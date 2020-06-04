import logging

import connexion
from flask import Flask


API_DEFINITION_PATH = './openapi.yml'

# Config variables that can be overridden with envvars
CUSTOM_CONFIG = {
    'BRAINTREE_MERCHANT_ID': 'dummy',
    'BRAINTREE_PUBLIC_KEY': 'dummy',
    'BRAINTREE_PRIVATE_KEY': 'dummy',
    'ENVIRONMENT': 'sandbox',  # for prod use: 'production' 
}


def create_app(config: dict) -> connexion.FlaskApp:
    logging.basicConfig(level=logging.DEBUG)

    parsed_config = {
        key: config.get(key, default_value)
        for key, default_value in CUSTOM_CONFIG.items()
    }

    app = connexion.FlaskApp(__name__)
    app.add_api(API_DEFINITION_PATH)
    app.app.config.update(parsed_config)

    return app
