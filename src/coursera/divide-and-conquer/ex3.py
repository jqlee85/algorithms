import unittest
import random
import sys



text_file = open("./ex3input.txt", "r")
list1 = text_file.read().splitlines()
for i in range(len(list1)):
  list1[i] = int(list1[i])

compareCount = 0

def quicksort(arr,l=False,r=False,pivotType='rand'):
  print('----')
  
  global compareCount 

  #set l,r for initial call
  if (not(l) and not(r)):
    l = 0
    r = len(arr) - 1

  print('size: ',str(r-l))
  if (r-l != len(arr)):
    compareCount += (r - l)

  print('subsection:',arr[l:r+1])

  
  # base case
  if (r-l < 2): 
    return

  pivot = choosePivot(l,r,pivotType)
  pivotValue = arr[pivot]
  [left,right] = partition(arr,l,r,pivot)
  quicksort(arr,left[0],left[1],pivotType)
  quicksort(arr,right[0],right[1],pivotType)
  return arr

def partition(arr,l,r,pivot):
  
  #swap pivot to beginning
  pivotValue = arr[pivot]
  first = arr[l]
  arr[pivot] = first
  arr[l] = pivotValue

  # print('pivot',pivot)
  print('pivot:',pivot,pivotValue)

  print('beforepartition:',arr[l:r+1]) 

  i = l+1
  print('l',l)
  print('i',i)
  print('r',r)
  for j in range(l+1,r+1):
    if (arr[j] < pivotValue):
      #swap first largest with the current
      firstLarge = arr[i]
      current = arr[j]
      arr[i] = current
      arr[j] = firstLarge
      #increment divider between smaller and larger sections
      i += 1
      # print('i=>',i)
    #else:
      # print(arr[j])
  print('l',l)
  print('i',i)
  print('r',r)  

  #swap pivot into correct place
  lastSmall = arr[i-1]
  arr[i-1] = pivotValue
  arr[l] = lastSmall



  left = [l,i-1]
  right = [i,r]
  print('afterpartition:',arr[l:r+1]) 
  print('left',l,i-1)
  print('left',arr[l:i-1])
  print('right',i,r)
  print('right',arr[i:r+1])

  return [left,right]


def choosePivot(l,r, pivotType='rand'):
  
  if (pivotType == 'first'):
    return l
  elif (pivotType == 'last'):
    return r
  else:
    return random.randrange(l,r)




# class TestQuicksort(unittest.TestCase):
#   def test(self):
#     self.assertEqual(quicksort([4,5,9,4,10,6,5,3,7,8,3,7,1,2,5,7,3,2,1],False,False,'first'),[1,1,2,2,3,3,3,4,4,5,5,5,6,7,7,7,8,9,10])




# theTest = TestQuicksort()
# theTest.test()

sample = [4,5,9,4,10,6,5,3,7,8,3,7,1,2,5,7,3,2,1]
print(quicksort(sample,False,False,'rand'))


# sys.setrecursionlimit(max(sys.getrecursionlimit(), len(list1)+10000))

# print(sys.getrecursionlimit())

# sortedArr = quicksort(list1,False,False,'first')
# print(sortedArr)
# print('compareCount '+str(compareCount))

#rand comparecount 161265
#last comparecount 17180884


