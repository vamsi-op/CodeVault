for _ in range(int(input("Enter number of test cases: "))):
    try:
        x = int(input("Enter number: "))
        flag = True if x < 0 else False
        x *= -1 if flag else 1
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
            
        print(-res if flag else res)
    except ValueError:
        print("Enter a valid number")
