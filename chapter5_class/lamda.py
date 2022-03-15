# An expression evaluates to a value
# A statement executes something
# The evaluation of a statement does not changes state
# The execution of a statement changes state
# Evaluation of an expression always Produces or returns a result value.
# Execution of a statement may or may not produces or displays a result value, 
# it only does whatever the statement says

#############################
# callale
############################

import random
class BingoCage:
  def __init__(self, items):
    self._items = list(items)
    random.shuffle(self._items)
  def pick(self):
    try:
      return self.