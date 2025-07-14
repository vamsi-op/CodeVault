for _ in range(int(input("Enter number of test cases: "))):
    try:
        n = int(input("Enter a Number: "))
        org, length = n, 0
        digits = []
        # store digits and calculate length
        while n > 0:
            digits.append(n % 10)
            n = n//10
            length += 1
        
        n = sum(digit**length for digit in digits)

        print("Yes" if org == n else "No")
    except ValueError:
        print("Invalid Input")
