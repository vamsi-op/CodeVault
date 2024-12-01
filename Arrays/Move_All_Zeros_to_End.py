#test cases
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    p = 0 #pointer that points to first occurence of 0's index
    n = len(arr)
    for i in range(n):
            if arr[i] != 0:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1
    print(arr)
