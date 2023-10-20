"""
  Term Class
  @author Lehrman, Aidin
"""

from __future__ import anotations

class Term:
	def __init__(self, coefficient, exponent) -> None:
		self.coefficient: float = coefficient
		self.exponent: float = exponent

	def eval_at(x: float) -> float:
		return self.coefficeint * (x ** self.exponent)

	def as_lambda(self) -> lambda:
    	return lambda x: self.eval_at(x)

  	def __add__(a: Term: b: Term):
    	pass
