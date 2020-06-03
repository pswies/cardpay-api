import mock

import pytest

from payments import BraintreeProvider


@pytest.fixture
def provider():
    provider = BraintreeProvider(
        merchant_id='merchant-123',
        public_key='public-123',
        private_key='private-123',
    )
    provider._gateway = mock.Mock()

    customer_result = mock.Mock()
    customer_result.customer.id = 'customer-123'
    provider._gateway.customer.create.return_value = customer_result

    return provider


@pytest.fixture
def result_credit_card():
    result = mock.Mock()
    result.is_success = True
    result.credit_card.token = 'token-123'
    return result


@pytest.fixture
def result_sale():
    result = mock.Mock()
    result.is_success = True
    result.transaction.id = 'transaction-123'
    result.transaction.status = 'authorized'
    result.transaction.amount = '7.00'
    result.transaction.currency_iso_code = 'EUR'
    return result


@pytest.fixture
def result_failure():
    result = mock.Mock()
    result.is_success = False
    result.message = 'error-123'
    return result
