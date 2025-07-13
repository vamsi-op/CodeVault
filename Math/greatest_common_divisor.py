for _ in range(int(input("Enter number of test cases: "))):
    while True:
        try:
            a, b = map(int, input("Enter the two numbers(a b): ").split())
            while b:
                a, b = b, a % b
            print(a)
            break
        except ValueError:
            print("Invalid input")
'''
Constraints:
number > 0
'''
