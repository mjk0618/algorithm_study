# 변환 dictionary 정의
symbol = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

# 입출력 변수 정의
integer = list(input())
roman = []

unit = 1

# roman list 작성
while integer:
    num = int(integer.pop())
    num = divmod(num, 5)
    temp = []
    if num[1] == 4:
        if num[0] == 1:
            temp += [1, 10]
        elif num[0] == 0:
            temp += [1, 5]
    else:
        if num[0] ==1:
            temp += [5]
        temp += [1] * num[1]
    temp = [(i * unit) for i in temp]
    roman.append(temp)
    unit *= 10

roman.reverse()
        
# Int to roman symbol 변환
for i in range(0, len(roman)):
    for j in range(0, len(roman[i])):    
        roman[i][j] = symbol[roman[i][j]]

roman = sum(roman, [])
roman = ''.join(roman)

print(roman)