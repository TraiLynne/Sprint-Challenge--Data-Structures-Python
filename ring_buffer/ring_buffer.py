class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass
    # Set the current index of storage as the item

    # if the current index is less than the capacity (minus 1 because of how indexes are numbered), 
    #   move to the next index, 
    # else 
    #   start over

  def get(self):
    # For each element in storage, add element to list if item != None. Return list
    return [i for i in self.storage if i != None] 