"""
    Polynomial Class
    @author Lehrman, Aidin
"""

from term import Term

class Polynomial:
    """ A Polynomial is a list of added together terms
        Format:
            (a * (x ** n)) + (b * (x ** (n-1))) + ... + (y * (x ** 1)) + (z * (x ** 0))

        Values:
            Coeffiecients: 'a-z' are floats in range (-inf, inf)
            Exponents: 'n-0' are floats in range [0, inf)

        Args:
            *terms (list[Term] | None): All terms that will be added together to form the Polynomial
    """
    def __init__(self, *terms: list[Term] | None) -> None:
        pass