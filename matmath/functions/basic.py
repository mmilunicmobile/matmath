from operation import Operation

class Constant(Operation):
  def __init__(value):
    super().__init__(
      lambda self : str(self.values[0]),
      lambda self : Constant(0),
      lambda self, e : self.values[0],
      value
    )