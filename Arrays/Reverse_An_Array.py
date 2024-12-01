#test cases
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    print(arr)
