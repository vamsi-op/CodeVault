# Inverted Right Triangle pattern

def pat(n):
    # decrement loop
    for i in range(n, 0, -1):
        for j in range(i):
            print(f"{j + 1} ", end="") # end argument allows us skip new line
        print() # move to new line

for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
