from flask import abort, jsonify, request

from api.helpers import make_payment_provider
from payments import PaymentError


def ping():
    return jsonify(reply='pong')


def tokenise(body):
    """Generate a token representing a card."""
    provider = make_payment_provider()

    try:
        token = provider.tokenise_card(body['card_number'], body['expiry_date'])
    except PaymentError as e:
        abort(400, str(e)) 

    return jsonify(token=token)


def sale(body):
    """Make card payment using a token."""
    provider = make_payment_provider()

    try:
        transaction = provider.make_sale(body['token'], body['amount'])
    except PaymentError as e:
        abort(400, str(e)) 

    return jsonify(transaction.serialize())
