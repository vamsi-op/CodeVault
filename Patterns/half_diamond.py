# Diamond Pattern

def pat(n):
    # print first half of diamond
    for i in range(n):
        for j in range(i + 1):
            print("# ", end="")
        print() # new line

    # print seccond half of diamond
    for i in range(n - 1):
        for j in range(n - i - 1):
            print("# ", end="")
        print() # new line
    
for _ in range(int(input("Enter number of test cases: "))):
  try:
    n = int(input("Enter number of rows: "))
    pat(n)
  except ValueError:
    print("Enter a valid number")
