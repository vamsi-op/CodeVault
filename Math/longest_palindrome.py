from collections import Counter

for _ in range(int(input("Enter number of test cases: "))):
    s = input("Enter string: ").lower()
    mp = Counter(s)
    res = 0
    has_odd = False
    for key in mp:
        if mp[key] % 2 == 0:
            res += mp[key]
        else:
            res += mp[key] - 1
            if not has_odd:
                has_odd = True
    print(res + 1 if has_odd else res)
'''
Constraints:

i in s[i] is alphanumeric
'''
