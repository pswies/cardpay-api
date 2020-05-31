# tokenpay-api

A Python API for token-based payments.

It uses Braintree (braintreepayments.com) as the payment provider.
This, however, should be easy to replug.


## Prerequisites

Installed Docker.


## Building and running

It should be enough to run:

    docker build -t tokenpay-api .
    docker run --rm -it -p 8080:80 -v $(pwd):/app tokenpay-api

Ensure that it works with:

    curl localhost:8080  # should greet the world


## Todo

* Add tests
* Check coverage
* Use linter
