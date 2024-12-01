# Test cases
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n = len(arr)
    # For indices, m will store the index to start reversing from
    # o will store the index of the element to swap
    m = o = 0 
    # Find the first decreasing pair starting from the end of the array
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            m = i
            break
    # If no such pair is found, reverse the entire array
    if m == 0:
        arr.reverse()
    else:
        # Find the smallest element greater than arr[m-1] after index m
        o = m
        for i in range(m + 1, n):
            if arr[o] > arr[i] and arr[i] > arr[m-1]:
                o = i
        # Swap arr[m-1] and arr[o]
        arr[m - 1], arr[o] = arr[o], arr[m- 1]
        # Calculate the number of elements to reverse after index m
        q = (n-m)//2
        # Reverse the subarray from index m to the end
        for i in range(q):
            arr[m + i], arr[n - 1 - i] = arr[n - 1 -i], arr[m + i]
    print(arr)
