# cardpay-api

A Python API for token-based card payments.

It uses Braintree (braintreepayments.com) as the payment provider.
This, however, can be easy replugged if needed.


## Prerequisites

Installed Docker.


## Usage

Build the Docker container:

    cd <project_dir>
    docker build -t cardpay-api .

Create `container.env` file with the following content:

    BRAINTREE_MERCHANT_ID=<your-value>
    BRAINTREE_PUBLIC_KEY=<your-value>
    BRAINTREE_PRIVATE_KEY=<your-value>
    ENVIRONMENT=sandbox

Launch the HTTP API for development:

    docker run -it --rm -p 8080:80 -v $(pwd):/app --env-file ./container.env cardpay-api

Ensure that it works:

    curl localhost:8080  # should greet the world

Example user session:

    $ curl -X POST localhost:8080/tokenise -H "Content-type: application/json" -d '{"card_number": "4111111111111111", "expiry_date": "06/2022"}'
    {"token":"f4jp8wm"}
    $ curl -X POST localhost:8080/sale -H "Content-type: application/json" -d '{"token": "f4jp8wm", "amount": "7.99"}'
    {"amount":"7.99","currency":"EUR","id":"2sang9v1","status":"authorized"}

Production deployment details are beyond the scope of this documentation.


## Todo

* Use OpenAPI
* Add tests
* Check coverage
* Use linter
* Ensure typehints
* Add `created_at` to `PaymentTransaction`
