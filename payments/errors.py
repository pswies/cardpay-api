"""
Error handling in its current form is very basic.
More specific error classes should be used in a production scenario.
"""

class PaymentError(Exception):
    """A base class for all payment-related errors."""
    pass
