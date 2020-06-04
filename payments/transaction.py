from decimal import Decimal


class PaymentTransaction:
    """
    A model class representing a vendor-independent result of a sale.

    Fields:
    * id: Transaction ID string.
    * status: String describing the current state of the transaction
      in the context of the payment's lifecycle.
    * amount: Internally - a decimal containing the paid amount; converted
      to string only during serialization.
    * currency: ISO currency string.
    """

    def __init__(self, transaction_id: str, status: str, amount: Decimal, currency: str):
        self.id = transaction_id
        self.status = status
        self.amount = amount
        self.currency = currency

    def serialize(self) -> dict:
        """
        Convert the object into a dict containing only serializable values.

        In particular, the result is parsable by the default Python JSON encoder.
        The money amount is converted to string to avoid floating point-related caveats.
        """
        return {
            'id': self.id,
            'status': self.status,
            'amount': str(self.amount),
            'currency': self.currency,
        }
