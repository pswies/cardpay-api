import os

from api.flaskapp import create_app


app = create_app(os.environ)
