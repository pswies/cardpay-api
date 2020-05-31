import os

from tokenpay.flaskapp import create_app


app = create_app(os.environ)
