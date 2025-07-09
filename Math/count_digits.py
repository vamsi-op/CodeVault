for _ in range(int(input("Enter number of test cases: "))):
    n = int(input("N: "))
    res = 1
    while n > 9:
        res += 1
        n //= 10
    print(res)
