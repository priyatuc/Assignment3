import random

def quickSort(arr):
  if len(arr)<=1: return arr

 # Choose a random pivot
  pivotIndex = random.randint(0, len(arr) - 1) 
  pivot = arr[pivotIndex]
  left = []
  right = []
  middle = []

  for i in range(len(arr)):
    if arr[i] < pivot:
        left.append(arr[i])
    elif arr[i] == pivot:
        middle.append(arr[i])
    else:
        right.append(arr[i])

#recursively sort left and right, then combine
  return quickSort(left) + middle + quickSort(right)

arr = [9,8,7,6,5,4,3,2,1]
print ("The original array is:", arr)
print ("The sorted array is:", quickSort(arr))
