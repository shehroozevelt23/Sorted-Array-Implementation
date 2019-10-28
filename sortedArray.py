from math import floor

class Pair:
  # Pair(self, key, element) creats a pair containing key & element 
  # Pair: Any Any -> Pair
  def __init__(self, key, element):
    self._key = key
    self._element = element
  
  # self.get_key() returns key value of self 
  # get_key: Pair -> Any 
  def get_key(self):
    return self._key
  
  # self.get_element(self) returns element of self 
  # get_element: Pair -> Any
  def get_element(self):
    return self._element
  
  # self.__str()__ creates a string representation of Pair self 
  # __str__: Pair -> Str 
  def __str__(self):
    s = "(" + str(self._key) + "," + str(self._element) + ")"
    return s

# guess(low, high, search, length) determines the next item to compare during interpolation search 
# guess: Nat Nat Int Nat -> Nat
def guess(low, high, search, length):
  val = floor((search - low)/(high - low) * length)
  val = max(val, 0)
  val = min(val, length)
  return val

class SortedArray:
  
    # SortedArray(capacity) creates an empty SortedArray with space for capacity elements 
    # __init__: Nat -> SortedArray 
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._cap  = capacity
        self._size = 0
    
    # self.is_empty() returns a boolean value based on whether or not self is empty 
    # is_empty: SortedArray -> Bool
    def is_empty(self):
      return self._size == 0
    
    # self.--- returns a boolean value based on whether or not item is in self 
    # __contains__: SortedArray Int -> Bool 
    def __contains__(self, item):
      for i in range(self._cap):
        if self._items[i] == item:
          return True 
      return False 
    
    # self.access(index) returns the value stored at index in self 
    # access: SortedArray Nat -> Int 
    def access(self, index):
      return self._items[index] 
    
    # self.linear_search(item) returns a pair, the key being the index at which the item may be stored 
    # and the element being the number of items checked using linear search 
    # linear_search: SortedArray Int -> Pair
    def linear_search(self, item): 
      if self.is_empty() == True:
        return Pair(0,0)      
      index = 0
      count = 1
      
      while (self._items[index] != None) and (self._items[index] < item):
        count += 1
        index += 1
        
      return Pair(index,count)    
     
    
    # self.binary_search(item) returns a pair, the key being the index at which the item may be stored 
    # and the element being the number of items checked using binary search 
    # binary_search: SortedArray Int -> Pair    
    def binary_search(self, item):
      if self.is_empty() == True:
        return Pair(0,0)
      
      count = 0
      absent_count = 0
      index = 0
      begin = 0
      end = self._size - 1
      while begin <= end:
        mid = floor(begin + (end - begin)/2)
        
        if begin == end:
          absent_count = begin
        
        if self._items[mid] == item:
          index = mid  
          count += 1
          break
        
        elif self._items[mid] < item:
          begin = mid + 1
          count += 1
          
        else:
          end = mid - 1
          count += 1
          
      if index == 0:
        p = Pair(absent_count, count)
      else:
        p = Pair(index, count)
      return p 
    
    # self.interpolation_search(item) returns a pair, the key being the index at which the item may be stored 
    # and the element being the number of items checked using interpolation search 
    # interpolation_search: SortedArray Int -> Pair    
    def interpolation_search(self, item):
      if self.is_empty() == True:
        return Pair(0,0)      
      count = 0
      index = 0
      begin = 0
      end = self._size - 1
      while begin <= end:
        first = self._items[begin]
        last = self._items[end]
        if first == last:
          if item <= first:
            count += 1
            index = begin 
            p = Pair(index, count)
            return p             
          else:
            count += 1
            index = end + 1
            p = Pair(index, count)
            return p             
        mid = begin + guess(first, last, item, end - begin)
        if self._items[mid] == item:
          count += 1
          index = mid 
          p = Pair(index, count)
          return p           
        elif item > self._items[mid]:
          count += 1
          begin = mid + 1
        elif item < self._items[mid]:
          count += 1
          end = mid - 1
      index = begin 
      p = Pair(index, count)
      return p     
    
    # self.add(item) stores an instance of item in self 
    # add: SortedArray Int -> None 
    # Effects: Mutates self to contain a single instance of item 
    def add(self, item):
      index = 0
      for i in range(0, self._cap):
        if self._items[i] == None:
          self._items[i] = item 
          self._size += 1
          return
        if self._items[i] > item:
          index = i
          break 
      j = self._size
      while (j > index):
        self._items[j] = self._items[j-1]
        j -= 1
  
      self._items[index] = item 
      self._size += 1
    
    # self.delete(item) removees an instance of item from self 
    # delete: SortedArray Int -> None
    # Effects: Mutates self to have an instance of item removed from it 
    def delete(self, item):
      p_search = self.binary_search(item)
      p = p_search.get_key()
      for i in range(p, self._size):
        self._items[i] = self._items[i+1]
      self._size -= 1
    
    
    
          
    
    
  
  