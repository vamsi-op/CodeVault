def check_pow_of_two(n):
    if n < 1:
        return False
    """ The core logic of n & (n - 1) == 0.
    This bitwise trick works because if 'n' is a power of two, its binary representation
    has a single '1' bit (e.g., 8 is 1000). 
    Subtracting 1 from 'n' flips that '1' bit to '0' and all trailing '0' bits to '1'
    (e.g., 8 - 1 = 7 is 0111).
    Performing a bitwise AND on 'n' and 'n - 1' will result in 0 """
    if n & (n - 1) == 0:
        return True
    else:
        return False


num = None
try:
    num = int(input("Enter a  number: "))
except ValueError:
    print("Enter a valid number")

if num != None:
    print(check_pow_of_two(num))
