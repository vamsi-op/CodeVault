# Pyramid Pattern

def pat(n):
    for i in range(n):
        # print blanks
        for j in range(n - i - 1):
           print(" ", end="")
        # print '#'
        for j in range(i + 1 ):
            print("# ", end="")
        print()
    

for _ in range(int(input("Enter number of test cases: "))):
  try:
    n = int(input("Enter number of rows: "))
    pat(n)
  except ValueError:
    print("Enter a valid number")
