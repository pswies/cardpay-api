from flask import Blueprint


base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/', methods=['GET'])
def get_home():
    """Default route that does nothing."""
    return 'Hello, world!\n', 200
