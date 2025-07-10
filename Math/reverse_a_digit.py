for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter a number: "))
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n = n // 10
        print(res)
    except ValueError:
        print("Enter a valid number")
