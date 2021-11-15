class Operation:
  def __init__(self, string, derivative, evaluate, *values):
    self.__str__ = string;
    self.derivative = derivative;
    self.evaluate = evaluate
    self.values = values