# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
import math

class MinHeap:
  def __init__(self, array):
      # Do not edit the line below.
      self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    # newArray = [None] * len(array)
    self.heap = array
    for i in reversed(range(len(array))):
      self.siftDown(i)

    print('newArray',self.heap)
    return self.heap
	
	
		

  def siftDown(self,currentIdx,existingIdx=0):
    current = self.heap[currentIdx]
    print('siftDown:'+str(current)+' idx:'+str(existingIdx))
    print(self.heap)
    existing = self.heap[existingIdx]
    
    if (existing is None): self.heap[existingIdx] = current
    elif (current < existing):
      print('c:'+str(current)+'<'+'e:'+str(existing))
      self.swap(currentIdx,existingIdx)
      print('afterswap:'+str(self.heap))


    # get smaller idx
    leftIdx = self.getleftIdx(existingIdx)
    rightIdx = self.getrightIdx(existingIdx)
    if (leftIdx >= len(self.heap)):
      return None
    elif (rightIdx >= len(self.heap)):
      smallerIdx = leftIdx
    else: 
      leftValue = self.heap[leftIdx] 
      rightValue = self.heap[rightIdx]
      print('l:'+str(leftValue)+' r:'+str(rightValue))
      if (leftValue <= rightValue): smallerIdx = leftIdx
      else: smallerIdx = rightIdx  
    self.siftDown(currentIdx,smallerIdx)
    
      
      
    
				

  def siftUp(self,currentIdx):
    parentIdx = getParentIdx(currentIdx)
    if (parentIdx >= 0 && self.heap[currentIdx] < self.heap[parentIdx]):
      self.swap(currentIdx,parentIdx)
      self.siftUp(parentIdx)

  def peek(self):
    return self.heap[0]

  def remove(self):
      # Write your code here.
    return None


  def insert(self, value):
      # Write your code here.
    return None

  def getParentIdx(self,childIdx):
    # 1 > 0
    # 2 > 0
    # 3 > 1
    # 4 > 1
    # 5 > 2
    # 6 > 2
    # 7 > 3
    # 8 > 3
    # 9 > 4
    # 10 > 4
    if (childIdx % 2 == 0):
      return childIdx / 2 - 1
    else:
      return math.ceil(childIdx/2) - 1
		
  def getleftIdx(self,parentIdx):
    return parentIdx * 2 + 1

  def getrightIdx(self,parentIdx):
    return parentIdx * 2 + 2

  def swap(self,idxA,idxB):
    print('Swap: a:'+str(self.heap[idxA])+' b:'+str(self.heap[idxB]))
    temp = self.heap[idxA]
    self.heap[idxA] = self.heap[idxB]
    self.heap[idxB] = temp