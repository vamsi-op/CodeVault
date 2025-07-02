num = None
try:
    num = int(input("Enter a  number: "))
except ValueError:
    print("Enter a valid number")

if num != None:
    if num < 1:
        print("False")
        
    if num & (num - 1) == 0:
        print("True")
    else:
        print("False")
