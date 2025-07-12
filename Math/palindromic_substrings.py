for _ in range(int(input("Enter number of test cases: "))):
    s = input("Enter string: ").lower()
    n, res = len(s), 0
    for i in range(n):
        for l, r in [(i, i),(i, i+1)]:
            while l >= 0 and r < n and s[l] == s[r]: l -= 1; r += 1
            res += (r-l)//2
    print(res)

'''
Input: aaa
Output: 6
a, a, a, aa, aa, aaa

Constraints:
s[i] is an alphanumeric character
'''
