# Hollow rectangle pattern
def pat(x, y):
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                print('# ', end="")
            else:
                print('  ', end="")
        print() # move to new line

for _ in range(int(input("Enter number of test cases: "))):
    try:
        x = int(input("Enter rows count ( > 2): "))
        y = int(input("Enter columns count ( > 2): "))
        pat(x, y)
    except ValueError:
        print("Enter valid number")
