# Butterfly Pattern

def pat(n):
    # first half
    for i in range(1, n + 1):
        # print left half of the butterfly
        for j in range(i):
            print("# ", end="")
        # print spaces
        for j in range(2 * (n - i)):
            print("  ", end="")
        # print right half of the butterfly
        for j in range(i):
            print("# ", end="")
        print() # print new line
    # second half
    for i in range(1, n):
        # print left half of the butterfly
        for j in range(n - i):
            print("# ", end="")
        # print spaces
        for j in range(2 * i):
            print("  ", end="")
        # print right half of the butterfly
        for j in range(n - i):
            print("# ", end="")
        print() # print new line
    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter size of Butterfly: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
