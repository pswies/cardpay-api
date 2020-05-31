"""
This module contains an implementation of payments logic using Braintree.

Implementation note: one may argue that naming this module 'braintree' is an error
due to the name clash with the 'braintree' library. This was a conscious decision
based on the belief in the power of namespaces and superiority of concise names.
"""

import braintree

from payments.base import PaymentProvider
from payments.errors import PaymentError
from payments.transaction import PaymentTransaction


class BraintreeProvider(PaymentProvider):
    """An interface for Braintree's payment gateway."""

    def __init__(
        self,
        merchant_id: str,
        public_key: str,
        private_key: str,
        use_sandbox: bool = False,
    ):
        """
        Initialise a basic Braintree connection.

        See: https://developers.braintreepayments.com/start/hello-server/python
        """
        environment = (
            braintree.Environment.Sandbox if use_sandbox
            else braintree.Environment.Production
        )

        self._gateway = braintree.BraintreeGateway(
            braintree.Configuration(
                environment,
                merchant_id=merchant_id,
                public_key=public_key,
                private_key=private_key,
            )
        )

    def tokenise_card(self, card_number: str, expiry_date: str) -> str:
        """
        Tokenise a card.

        Note the lack of customer ID. It is being generated ad hoc.
        See base method description for details.
        """
        customer_id = self._gateway.customer.create().customer.id

        result = self._gateway.credit_card.create({
            "customer_id": customer_id,
            "number": card_number,
            "expiration_date": expiry_date,
        })

        if result.is_success:
            return result.credit_card.token
        else:
            raise PaymentError(result.message)


    def make_sale(self, token: str, amount: str) -> PaymentTransaction:
        """
        Make card payment using a token.

        See base method description for details.
        """
        result = self._gateway.transaction.sale({
            "payment_method_token": token,
            "amount": amount,
        })

        if result.is_success:
            return PaymentTransaction(
                result.transaction.id,
                status=result.transaction.status,
                amount=result.transaction.amount,
                currency=result.transaction.currency_iso_code,
            )
        else:
            raise PaymentError(result.message)
