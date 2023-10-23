"""
  Term Class
  @author Lehrman, Aidin
"""

from __future__ import annotations
#from polynomial import Polynomial

class Term:
    """ A Term is a ('coefficient' * ('x' ** 'exponent'))
    
    Attributes:
        coefficient (float): A constant value that is multiplied to 'x' after 'x' is exponentialized
        exponent (float):  The expoenent in which 'x' is raised to when self.eval_at(x) is called
	"""

    def __init__(self: Term, coefficient, exponent) -> None:
        """ Initializes a Term with values 'coefficient' and 'exponent'

        Args:
            coefficient (float): A constant value that is multiplied to 'x' 
                after 'x' is exponentialized
            exponent (float):  The expoenent in which 'x' is raised to when 
                self.eval_at(x) is called
        """
        self.coefficient: float = coefficient
        self.exponent: float = exponent

    def __str__(self: Term) -> str:
        return f'[{self.coefficient} * (x ** {self.exponent})]'

    def eval_at(self: Term, x: float | int) -> float:
        """	Evaluates term at x-value 'x'
        
        Args:
            x (float): The value at which you want to evaluate the term at.

        Returns:
            A float that is the value of the Term after it is evaluated at 'x'
        """
        return self.coefficient * (x ** self.exponent)

    #def __add__(self, other_term: Term) -> Polynomial:
        """ Adds two Terms together

        Args:
            other_term (Term): Term to add to self

        Returns:
            A Polynomial with terms 'self' and 'other_term'
        """
        #return Polynomial(self, other_term)
    
    #def __sub__(self, other_term: Term) -> Polynomial:
        """ Subtracts two Terms

        Args:
            other_term (Term): Term to subtract from self

        Returns:
            A Polynomial with terms 'self' and 'other_term'
        """
        #return Polynomial(self, other_term)
