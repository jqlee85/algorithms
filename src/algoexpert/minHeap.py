import math

# Minimum Heap Class
class MinHeap:
  def __init__(self, array):  
    self.heap = self.buildHeap(array)
    self.dataType = 'int'

  def buildHeap(self, array, dataType='int'):
    self.dataType = dataType
    self.heap = array
    for i in reversed(range(len(array))):
      self.siftDown(i)
    return self.heap

  def siftDown(self,currentIdx):
    current = self.heap[currentIdx]
    leftIdx = self.getLeftIdx(currentIdx)
    rightIdx = self.getRightIdx(currentIdx)
    
    # No children, done
    if (leftIdx >= len(self.heap)):
      return None
    # No right child, check left
    elif (rightIdx >= len(self.heap)):
      smallerIdx = leftIdx
    # Compare to get smaller
    else: 
      if (self.dataType == 'djikstra'): leftValue = self.heap[leftIdx][1] 
      else: leftValue = self.heap[leftIdx] 
      if (self.dataType == 'djikstra'): rightValue = self.heap[rightIdx][1] 
      else: rightValue = self.heap[rightIdx] 
      if (leftValue <= rightValue): smallerIdx = leftIdx
      else: smallerIdx = rightIdx  
    
    # If current is smaller than the smaller of the children, swap and siftDown again
    if (self.heap[currentIdx] > self.heap[smallerIdx]):
      self.swap(currentIdx,smallerIdx)
      self.siftDown(smallerIdx)
    

  def siftUp(self,currentIdx):
    parentIdx = self.getParentIdx(currentIdx)
    if (self.dataType == 'djikstra'): currentValue = self.heap[currentIdx][1] 
    else: currentValue = self.heap[currentIdx] 
    if (self.dataType == 'djikstra'): parentValue = self.heap[parentIdx][1] 
    else: parentValue = self.heap[parentIdx] 
    
    if (parentIdx >= 0 and currentValue < parentValue):
      self.swap(currentIdx,parentIdx)
      self.siftUp(parentIdx)

  def peek(self):
    return self.heap[0]

  def remove(self):
    removed = self.heap[0]
    lastItem = self.heap.pop()
    self.heap[0] = lastItem
    self.siftDown(0)
    return removed

  def insert(self, value):
    newIdx = len(self.heap)
    self.heap.append(value)
    self.siftUp(newIdx)

  def getParentIdx(self,childIdx):
    return math.floor((childIdx-1)/2)
		
  def getLeftIdx(self,parentIdx):
    return parentIdx * 2 + 1

  def getRightIdx(self,parentIdx):
    return parentIdx * 2 + 2

  def swap(self,idxA,idxB):
    temp = self.heap[idxA]
    self.heap[idxA] = self.heap[idxB]
    self.heap[idxB] = temp