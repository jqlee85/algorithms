import unittest
import random
import sys
import math
import operator

debug = False
compareCount = 0

# Performs quicksort on a global array (in place)
def quicksort(l,r,pivotType='rand'):

  global arr
  global compareCount 
  global debug 
  
  length = r-l+1
  if (length <= 1): return

  # add to comparecount
  compareCount += length - 1
  
  pivot = choosePivot(l,r,pivotType)
  pivotVal = arr[pivot]
  [left,right] = partition(l,r,pivot)
    
  lengthLeft = left[1]-left[0]+1
  lengthRight = right[1]-right[0]+1

  if (lengthLeft > 0):
    quicksort(left[0],left[1],pivotType)
  
  if (lengthRight > 0):
    quicksort(right[0],right[1],pivotType)

  return arr

def partition(l,r,p):
  
  global arr
  
  # Swap pivot to first position
  pivotVal = swapPivot(l,p)

  i = l+1
  for j in range(l+1,r+1):
    if (arr[j] < pivotVal):
      # Swap first element known to be larger with the current
      current = arr[j]
      firstLarge = arr[i]
      arr[i] = current
      arr[j] = firstLarge
      # Increment divider between smaller and larger sections
      i += 1

  # Swap pivot into correct place
  lastSmall = arr[i-1]
  arr[i-1] = pivotVal
  arr[l] = lastSmall

  # Build arrays with pointers
  left = [l,i-2]
  right = [i,r]
  return [left,right]

# Swap pivot element with first of array section
def swapPivot(l,p):
  global arr
  pivotVal = arr[p]
  firstVal = arr[l]
  arr[l] = pivotVal
  arr[p] = firstVal
  return pivotVal

# Choose the pivot based on the type
def choosePivot(l,r, pivotType='first'):
  global arr
  global debug
  if (pivotType == 'first'):
    return l
  elif (pivotType == 'last'):
    return r
  elif (pivotType == 'med3'):
    middle = l + math.floor((r-l)/2)
    three = [(l,arr[l]),(middle,arr[middle]),(r,arr[r])]
    three.sort(key = operator.itemgetter(1))
    return three[1][0]
  else:
    return random.randrange(l,r+1)

#========= Test Cases =========#

### Actual Assignment input
text_file = open("./ex3input.txt", "r")
arr = text_file.read().splitlines()
for i in range(len(arr)):
  arr[i] = int(arr[i])
sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+10000))
sortedArr = quicksort(0,len(arr)-1,'med3')
print(sortedArr)
print('compareCount '+str(compareCount))
### first comparecount 162085
### last comparecount 164123
### med3 comparecount 138382


### large test case
# text_file = open("./ex3testcases/input_dgrcode_16_100000.txt", "r")
# arr = text_file.read().splitlines()
# for i in range(len(arr)):
#   arr[i] = int(arr[i])
# sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+10000))
# sortedArr = quicksort(0,len(arr)-1,'med3')
# print(sortedArr)
# print('compareCount '+str(compareCount))
### first should be 2127173 => 2127173
### last should be 2079088 => 2079088
### med3 should be 1749103 => 1749103

### small test case
# text_file = open("./ex3testcases/input_dgrcode_15_20.txt", "r")
# arr = text_file.read().splitlines()
# for i in range(len(arr)):
#   arr[i] = int(arr[i])
# sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+10000))
# sortedArr = quicksort(0,len(arr)-1,'med3')
# print(sortedArr)
# print('compareCount '+str(compareCount))
### first should be 69 => 69
### last should be 65 => 65
### med3 should be 56 => 56


### small test case
# text_file = open("./ex3testcases/input_dgrcode_10_10.txt", "r")
# arr = text_file.read().splitlines()
# for i in range(len(arr)):
#   arr[i] = int(arr[i])
# sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+10000))
# sortedArr = quicksort(0,len(arr)-1,'med3')
# print(sortedArr)
# print('compareCount '+str(compareCount))
### first should be 21 => 21
### last should be 22 => 22
### med3 should be 20 => 20

# class TestQuicksort(unittest.TestCase):
#   def test(self):
#     self.assertEqual(quicksort([4,5,9,4,10,6,5,3,7,8,3,7,1,2,5,7,3,2,1],False,False,'first'),[1,1,2,2,3,3,3,4,4,5,5,5,6,7,7,7,8,9,10])
# theTest = TestQuicksort()
# theTest.test()



