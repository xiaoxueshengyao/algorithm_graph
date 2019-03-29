def findSmallest(arr):
  smallest = arr[0]
  smallest_idx = 0
  for i in range(1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_idx = i
  return smallest_idx

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr
  #return should set after def

print selectionSort([5,3,6,22,10])
