def main():
    #test cases
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        d = int(input())
        n = len(arr)
        d %= n #handle d > n
        #rotation technique
        reverse(arr, 0, d - 1)
        reverse(arr, d, n-1)
        reverse(arr, 0, n-1)
        print(arr)

#reverse technique
def reverse(arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

main()
