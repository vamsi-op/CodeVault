# Repeated Alphabetical Half Pyramid Pattern

def pat(n):
    num = 0
    for i in range(n):
        # print left spaces
        for j in range(n - i - 1):
            print("  ", end="")
        # print alphabets    
        for j in range(i + 1):
            num = num % 26 # 0 to 25
            print(chr(65 + num), end=" ")
            num += 1
        num -= 2 # set num as decreasing variable
        for j in range(i):
            num = num % 26 # 0 to 25
            print(chr(65 + num), end=" ")
            num -= 1

        num = 0 # reset num to 0
        print() # print new line
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
