class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = [num_dict[i] for i in s ]
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                num[i] = -num[i]

        total = sum(num)
        return num, total

while True:
    flag = False
    s = input('Input Roman Number: ')
    for i in range(len(s)):
        if s[i] in ['I', 'V', 'X', 'L', 'C', 'D', 'M'] and i != len(s) - 1:
                continue
        elif s[i] in ['I', 'V', 'X', 'L', 'C', 'D', 'M'] and i == len(s) - 1:
            flag = True
            break
        else: 
            print('Re input value.')
            break
    if flag == True:
        break
       

sol = Solution().romanToInt(s)
print(sol)

'''
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''