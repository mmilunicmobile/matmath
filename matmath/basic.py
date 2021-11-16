from matmath.operation import Operation

class Constant(Operation):
  def __init__(self, value):
    super().__init__(
      lambda self : str(self.values[0]),
      lambda : Constant(0),
      lambda e : self.values[0],
      value
    )