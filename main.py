"""
    Main
    @author Lehrman, Aidin
"""

from term import Term
from polynomial import Polynomial

term: Term = Term(4, 3)
polynomial: Polynomial = Polynomial(term, Term(2, 3))

print(polynomial)
print(polynomial.derivative())