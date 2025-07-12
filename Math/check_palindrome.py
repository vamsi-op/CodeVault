for _ in range(int(input("Enter number of test cases: "))):
    s = input("Enter string: ").lower()
    res = True
    i, j = 0, len(s)
    while i < j:
        if s[i] != s[j]:
            res = False
    print(res)
'''
Constraints:

i in s[i] is alphanumeric
'''
