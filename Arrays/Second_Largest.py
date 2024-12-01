#test cases
t = int(input())
for i in range(t):
  arr = list(map(int, input().split()))
  n = len(arr)
  largest = -1
  secondLargest = -1
  for i in range(n):
        # If arr[i] > largest, update second largest with
        # largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        # If arr[i] < largest and arr[i] > second largest, 
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
  print(secondLargest)
