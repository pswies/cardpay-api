from decimal import Decimal


class PaymentTransaction:
    """
    A model class representing a vendor-independent result of a sale.

    Fields:
    * id: Transaction ID string.
    * status: String describing the current state of the transaction
      in the context of the payment's lifecycle.
    * amount: Decimal containing the paid amount.
    * currency: ISO currency string.
    """

    def __init__(self, transaction_id: str, status: str, amount: Decimal, currency: str):
        self.id = transaction_id
        self.status = status
        self.amount = amount
        self.currency = currency

    def to_dict(self) -> dict:
        """
        Convert the object into a serializable dict.

        In particular, the result is parsable by `json.dumps()`.
        """
        return {
            'id': self.id,
            'status': self.status,
            'amount': str(self.amount),
            'currency': self.currency,
        }
