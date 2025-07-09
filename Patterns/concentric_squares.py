# Concentric Square pattern
def pat(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            print(n - min(i, j, size - i - 1, size - j - 1), end=" ") # for reverse pattern just print min(i, j, size - i - 1, size - j - 1)
        print() # move to new line

for _ in range(int(input("Enter number of test cases: "))):
    try:
        x = int(input("Enter size: "))
        pat(x)
    except ValueError:
        print("Enter valid number")
