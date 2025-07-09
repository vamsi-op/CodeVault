for _ in range(int(input("Enter nber of test cases: "))):
    n = int(input("N: "))
    org = n
    res = 0
    while n > 0: # check digis from right
        digit = n % 10 
        if digit != 0 and org % digit == 0:
            res += 1
        n //= 10
    print(res)
