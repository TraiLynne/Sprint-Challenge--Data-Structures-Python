class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    # For each element in storage, add element to list if item != None. Return list
    return [i for i in self.storage if i != None] 