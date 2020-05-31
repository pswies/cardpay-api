import abc


class PaymentProvider(abc.ABC):
    """
    An abstract interface for communicating with a payment provider.
    """

    @abc.abstractmethod
    def tokenise_card(self, card_number: str, expiry_date: str) -> str:
        """
        Generate a token representing a card.

        Parameters:
        * card_number: 12-19 digit card number.
        * expiry_date: Card expiration date, format: 'MM/YY' or 'MM/YYYY'.

        Return value:
        A newly generated token - string used for making a sale.
        """
        pass

    @abc.abstractmethod
    def make_sale(self, token: str, amount: str) -> 'PaymentTransaction':
        """
        Make card payment using a token.

        The token is the result of card tokenisation that must occur prior to a sale.
        Note the lack of currency in params - this has to be configured separately.

        Parameters:
        * token: String representing a card.
        * amount: String expressing the billing amount, can contain numbers
          and one decimal point, e.g.: '10.35'.

        Return value:
        A PaymentTransaction object.
        """
        pass
