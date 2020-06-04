# cardpay-api

A Python API for token-based card payments.

It uses Braintree (braintreepayments.com) as the payment provider.
This, however, can be easy replugged if needed.


## Prerequisites

Installed Docker.


## Running tests

Build the Docker container with development capabilities:

    cd <project_dir>
    docker build --target development -t cardpay-api-dev .

Run tests, mounting current directory directly:

    docker run -it --rm -v $(pwd):/app cardpay-api-dev pytest --cov=api --cov=payments


## Local deployment

Build the Docker container without development capabilities (or simply use the dev one described above):

    cd <project_dir>
    docker build --target base -t cardpay-api .

Create `container.env` file with the following content:

    BRAINTREE_MERCHANT_ID=<your-value>
    BRAINTREE_PUBLIC_KEY=<your-value>
    BRAINTREE_PRIVATE_KEY=<your-value>
    ENVIRONMENT=sandbox

Launch the HTTP API locally:

    docker run -it --rm -p 8080:80 --env-file ./container.env cardpay-api

Ensure that it works:

    curl localhost:8080/ping

Example user session:

    $ curl -X POST localhost:8080/tokenise -H "Content-type: application/json" -d '{"card_number": "4111111111111111", "expiry_date": "06/2022"}'
    {"token":"f4jp8wm"}
    $ curl -X POST localhost:8080/sale -H "Content-type: application/json" -d '{"token": "f4jp8wm", "amount": "7.99"}'
    {"amount":"7.99","currency":"EUR","id":"2sang9v1","status":"authorized"}

For convenience a Swagger UI is available at `localhost:8080/ui` .

Production deployment details are beyond the scope of this documentation.
