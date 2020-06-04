from decimal import Decimal

import mock

from payments import PaymentError, PaymentTransaction


def test_ping(client):
    response = client.get('/ping')
    assert response.json == {'reply': 'pong'}


@mock.patch('api.helpers.BraintreeProvider.tokenise_card', return_value='a-token')
def test_tokenise_success(tokenise_card, client):
    response = client.post(
        '/tokenise',
        json={'card_number': '4111111111111111', 'expiry_date': '06/2022'},
    )

    assert response.status_code == 200
    tokenise_card.assert_called_once_with('4111111111111111', '06/2022')
    assert response.json == {'token': 'a-token'}


def test_tokenise_invalid_input_syntactic(client):
    response = client.post(
        '/tokenise',
        json={'card_number': 'lorem'},
    )
    assert response.status_code == 400


@mock.patch('api.helpers.BraintreeProvider.tokenise_card', side_effect=PaymentError('x'))
def test_tokenise_invalid_input_external(tokenise_card, client):
    response = client.post(
        '/tokenise',
        json={'card_number': '4111111111111111', 'expiry_date': '06/2022'},
    )
    assert response.status_code == 400
    assert response.json['detail'] == 'x'


@mock.patch('api.helpers.BraintreeProvider.make_sale')
def test_sale_success(make_sale, client):
    make_sale.return_value = PaymentTransaction(
        '123',
        status='status-x',
        amount=Decimal('11.22'),
        currency='EUR',
    )

    response = client.post(
        '/sale',
        json={'token': 'qwe123', 'amount': '5.50'},
    )

    assert response.status_code == 200
    make_sale.assert_called_once_with('qwe123', '5.50')
    assert response.json == {
        'id': '123',
        'status': 'status-x',
        'amount': '11.22',
        'currency': 'EUR',
    }


def test_sale_invalid_input_syntactic(client):
    response = client.post(
        '/sale',
        json={'token': None},
    )
    assert response.status_code == 400


@mock.patch('api.helpers.BraintreeProvider.make_sale', side_effect=PaymentError('x'))
def test_sale_invalid_input_external(make_sale, client):
    response = client.post(
        '/sale',
        json={'token': 'qwe123', 'amount': '5.50'},
    )
    assert response.status_code == 400
    assert response.json['detail'] == 'x'
