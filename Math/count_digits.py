for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("N: "))
        res = 1
        while n > 9:
            res += 1
            n //= 10
        print(res)

    except ValueError:
        print("Enter a valid number")

'''
Constraints:
0 <= n <= 10⁹
'''
