"""
  Term Class
  @author Lehrman, Aidin
"""

class Term:
  def __init__(self, coefficient, exponent) -> None:
    self.coefficient: float = coefficient
    self.exponent: float = exponent

  def eval_at(x: float) -> float:
    return self.coefficeint * (x ** self.exponent)
