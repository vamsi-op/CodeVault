# Repeated Alphabetical Half Pyramid Pattern

def pat(n):
    num = 0
    for i in range(n):
        for j in range(i + 1):
            num = num % 26 # 0 to 25
            print(chr(65 + num), end=" ")
        num += 1
        print()
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
