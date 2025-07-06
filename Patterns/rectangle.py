# print rectangle pattern
def pat(x, y):
    for i in range(x):
        for j in range(y):
            print('# ', end="") # end argument allows us skip new line
        print() # move to new line

for _ in range(int(input("Enter number of test cases: "))):
    try:
        x = int(input("Enter rows count: "))
        y = int(input("Enter columns count: "))
        pat(x, y)
    except ValueError:
        print("Enter valid number")
