# Inverted Alphabetical Half Pyramid Pattern

def pat(n):
    for i in range(n):
        for j in range(n - i):
            j = j % 26 # 0 to 25
            print(chr(65 + j), end=" ")
        print()
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
