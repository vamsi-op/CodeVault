# Hollow Diamond Pattern

def pat(n):
    # first half
    for i in range(n):
        for j in range(n - i):
            print("#", end="")
        for j in range(2 * i):
            print(" ", end="")
        for j in range(n - i):
            print("#", end="")
        print()
    # second half
    for i in range(n):
        for j in range(i + 1):
            print("#", end="")
        for j in range(2 * (n - i - 1)):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print()

    
for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter size of Daimond: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
