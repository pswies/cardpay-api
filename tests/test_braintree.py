import pytest

from payments import PaymentError


def test_tokenise_card_success(provider, result_credit_card):
    provider._gateway.credit_card.create.return_value = result_credit_card

    token = provider.tokenise_card('12345', '03/2025')

    provider._gateway.credit_card.create.assert_called_once_with({
        'customer_id': 'customer-123',
        'number': '12345',
        'expiration_date': '03/2025',
    })
    assert token == 'token-123'


def test_tokenise_card_failure(provider, result_failure):
    provider._gateway.credit_card.create.return_value = result_failure

    with pytest.raises(PaymentError) as error_info:
        provider.tokenise_card('12345', '03/2025')

    assert str(error_info.value) == 'error-123'


def test_make_sale_success(provider, result_sale):
    provider._gateway.transaction.sale.return_value = result_sale

    transaction = provider.make_sale('token-123', '3.14')

    provider._gateway.transaction.sale.assert_called_once_with({
        'payment_method_token': 'token-123',
        'amount': '3.14',
    })
    assert transaction.to_dict() == {
        'id': 'transaction-123',
        'status': 'authorized',
        'amount': '7.00',
        'currency': 'EUR',
    }


def test_make_sale_failure(provider, result_failure):
    provider._gateway.transaction.sale.return_value = result_failure

    with pytest.raises(PaymentError) as error_info:
        provider.make_sale('12345', '03/2025')

    assert str(error_info.value) == 'error-123'
