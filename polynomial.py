"""
    Polynomial Class
    @author Lehrman, Aidin
"""

from __future__ import annotations
from term import Term

class Polynomial:
    """ A Polynomial is a list of added together terms
        
        A Polynomial is multiple terms added together: 
            (a * (x ** n)) + (b * (x ** (n-1))) + ... + (y * (x ** 1)) + (z * (x ** 0))
            or
            (term_a) + (term_b) + ... + (term_y) + (term_z)

        Attributes:
            terms: List of terms (see: 'Term')
    """
    def __init__(self: Polynomial, *terms: list[Term | Polynomial] | None) -> None:
        """ A list of Terms added together

        Args:
            *terms (list[Term | Polynomial] | None): All terms that will be added together to form the Polynomial
        """
        if len(terms) == 0:
            self.terms: list[Term] = []
        else:
            self.terms: list[Term] = []
            for term in terms:
                if isinstance(term, Polynomial):
                    self.terms += term.get_terms()
                elif isinstance(term, Term):
                    self.terms.append(term)

    def __str__(self: Polynomial) -> str:
        """ Converts Polynomial to a String

        Args:
            None

        Returns:
            Formated string of Polynomial
        """
        string: str = str(self.terms[0])
        for i in range(1, len(self.terms)):
            string += f' + {self.terms[i]}'
        return f'({string})'

    def __add__(self: Polynomial, term: Term | Polynomial) -> Polynomial:
        """ Adds a Polynomial to another Polynomial/Term n=by initializing a new Polynomial
            with both terms

        Args:
            term (Term | Polynomial): The Term or Polynomial to add

        Retruns:
            Polynomial of both terms 'self' and 'term'
        """
        return Polynomial(self, term)
    
    def get_terms(self: Polynomial) -> list[Term]:
        """ Returns the Polynomial's Terms as a list

        Args:
            None

        Returns:
            List of terms
        """
        return self.terms
    
    def eval_at(self: Polynomial, x: float | int) -> float:
        """ Evaluates the Polynomial at value 'x'

        Args:
            x (float): Value of 'x' to evaluate the Polynomial at

        Returns:
            Float with value of Polynomial evaluated at a value of 'x'
        """
        sum: float = 0
        for term in self.terms:
            sum += term.eval_at(x)
        return sum
    
    def derivative(self) -> Polynomial:
        """ Calculates the derivative of a Polynomial
        
        Args:
            None
            
        Returns:
            Derivative of the Polynomial
        """
        derivative: Polynomial = Polynomial()
        
        term: Term
        for term in self.terms:
            new_coefficient: float = term.coefficient * term.exponent
            new_exponent: float = term.exponent - 1
            derivative += Term(new_coefficient, new_exponent)
        return derivative