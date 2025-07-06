# Half Butterfly Pattern

def pat(n):
    for i in range(1, n+1):
        # print left half of the butterfly
        for j in range(i):
            print(f"{j+1} ", end="")
        # print spaces
        for j in range(2 * (n - i)):
            print("  ", end="")
        # print right half of the butterfly
        for j in range(i):
            print(f"{j + 1} ", end="")
        print() # print new line
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
