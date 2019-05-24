class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # Set the current index of storage as the item
    self.storage[self.current] = item

    # if the current index is less than the capacity (minus 1 because of how indexes are numbered), move to the next index. Else, start over
    if self.current < self.capacity-1:
      self.current += 1
    else:
      self.current = 0

  def get(self):
    # For each element in storage, add element to list if item != None. Return list
    return [i for i in self.storage if i != None] 