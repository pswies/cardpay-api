from flask import current_app

from payments import BraintreeProvider


def make_payment_provider():
    config = current_app.config

    # It is unclear whether Braintree Gateway is thread-safe,
    # therefore no such global object is being used. Instead
    # it is being created at every call to API.
    return BraintreeProvider(
        merchant_id=config['BRAINTREE_MERCHANT_ID'],
        public_key=config['BRAINTREE_PUBLIC_KEY'],
        private_key=config['BRAINTREE_PRIVATE_KEY'],
        use_sandbox=(config['ENVIRONMENT'] != 'production'),
    )
