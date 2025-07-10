for _ in range(int(input("Enter number of test cases: "))):
    try:
        num = int(input("Enter a number: "))
        found = False
        for i in range(num + 1):
            if i + int(str(i)[::-1]) == num:
                found = True
                break
        print(found)
    except ValueError:
        print("Enter a valid number")

'''
Constraints:

0 <= num <= 105
'''
