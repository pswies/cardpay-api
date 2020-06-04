# === base stage ===

# We use Python 3.7 to ensure compatibility with Braintree.
# See: https://developers.braintreepayments.com/start/hello-server/python

FROM python:3.7-alpine AS base

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api ./api
COPY payments ./payments

CMD ["gunicorn", "-b", "0.0.0.0:80", "--log-level=info", "api.wsgi:app"]
EXPOSE 80


# === development stage ===

FROM base AS development

WORKDIR /app
COPY requirements-dev.txt .

RUN pip install -r requirements-dev.txt
