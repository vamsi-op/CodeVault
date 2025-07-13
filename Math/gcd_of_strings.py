for _ in range(int(input("Enter number of test cases: "))):
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")

    if s1 + s2 != s2 + s1:
        print("''")
    else:
        a, b = len(s1), len(s2) 
        while b: # find largest common length of substring
            a, b = b, a % b   
        print(s1[:a])
            
'''
Constraints:
1 <= |S1|, |S2| <= 1000
strings are case sensitive
'''
