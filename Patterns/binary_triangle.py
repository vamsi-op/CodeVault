# Binary Triangle Pattern

def pat(n):
    for i in range(n):
       for j in range(i + 1):
          if (i + j) % 2 == 0:
             print("1 ", end="")
          else:
             print("0 ", end="")
       print()
    
for _ in range(int(input("Enter number of test cases: "))):
  try:
    n = int(input("Enter number of rows: "))
    pat(n)
  except ValueError:
    print("Enter a valid number")
