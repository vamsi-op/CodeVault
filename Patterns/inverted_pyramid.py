# Inverted Pyramid Pattern

def pat(n):
    for i in range(n, 0, -1):
        # print blanks
        for j in range(n - i):
           print(" ", end="")
        # print '#'
        for j in range(i):
            print("# ", end="")
        print() # new line
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
