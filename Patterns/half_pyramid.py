# Half pyramid pattern

def pat(n):
    for i in range(n):
        for j in range(i + 1):
            print("# ", end="") # end argument allows us skip new line
    print() # move to new line

for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter number of rows: "))
        pat(n)
    except ValueError:
        print("Enter a valid number")
