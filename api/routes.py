from flask import Blueprint, jsonify, request

from api.helpers import make_payment_provider
from payments import PaymentError


base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/', methods=['GET'])
def home():
    return 'Hello, card payment world!\n'


@base_blueprint.route('/tokenise', methods=['POST'])
def tokenise():
    """Generate a token representing a card."""
    payload = request.json
    provider = make_payment_provider()
    token = provider.tokenise_card(payload['card_number'], payload['expiry_date'])
    return jsonify(token=token)


@base_blueprint.route('/sale', methods=['POST'])
def sale():
    """Make card payment using a token."""
    payload = request.json
    provider = make_payment_provider()
    transaction = provider.make_sale(payload['token'], payload['amount'])
    return jsonify(transaction.to_dict())
