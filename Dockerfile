# We use Python 3.7 to ensure compatibility with Braintree.
# See: https://developers.braintreepayments.com/start/hello-server/python

FROM python:3.7-alpine AS base
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app

FROM base
CMD ["gunicorn", "-b", "0.0.0.0:80", "--log-level=info", "--reload", "api.wsgi:app"]
EXPOSE 80
