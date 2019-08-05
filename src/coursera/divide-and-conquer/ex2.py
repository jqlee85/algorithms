# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
# Your task is to compute the number of inversions in the file given, where the i^{th} row of the file indicates the i^{th} entry of an array.
# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

def sortAndCount(nums):
  length = len(nums)
  if (length == 1): return [nums,0]
  else:
    # First half
    [b,x] = sortAndCount(nums[:length//2])
    # Second half
    [c,y] = sortAndCount(nums[length//2:])
    # Split Inversions
    [combined,z] = countSplitInv(b,c,length)    
    return [combined, x+y+z]

def countSplitInv(b,c,length):
  d = []
  i = 0
  j = 0
  count = 0
  for k in range(1,length+1):
    finishedB = (i >= len(b))
    finishedC = (j >= len(c))
    if (finishedB):
      d.append(c[j])
      j += 1
    elif (finishedC or b[i]<c[j]):
      d.append(b[i])
      i += 1
    else:
      d.append(c[j])
      count += (len(b) - (i))
      j += 1
  return [d,count]

# test1 = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
# [sortedArr,count] = sortAndCount(test1)
#should be 56

# test2 = [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]
# [sortedArr,count] = sortAndCount(test2)
#should be 590

# test3 = [ 4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]
# [sortedArr,count] = sortAndCount(test3)
#should be 2372

text_file = open("./ex2input.txt", "r")
list1 = text_file.read().splitlines()
for i in range(len(list1)):
  list1[i] = int(list1[i])
[sortedArr,count]  = sortAndCount(list1)
#should be 2407905288

print('FINAL ANSWER:' + str(count))