#### 1-1  세 정수의 최댓값 구하기
# 내풀이
from re import I


def max3():
    print('세 정수의 최댓값을 구합니다.')
    a, b, c = map(int, input('세 정수를 입력하세요 :').split())

    maximum = max([a,b,c])
    #print(f'최댓값은 "{maximum}"입니다.')
    return maximum
'''
# 책풀이
def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum # 최댓값 반환

print(f'max(3, 2, 1) = {max3(3, 2, 1)}')
'''


#### 1-2. 세 정수의 중앙값 구하기
## 내풀이
def median():
    num_list = list(map(int, input('세 정수를 입력하세요 :').split()))
    num_list.sort()
    if len(num_list) % 2 != 0:
        median = num_list[int(len(num_list)/2)]
    else:
        median = num_list[int(len(num_list)/2)-1 + int(len(num_list)/2)]
    return median, num_list

## 책풀이
# 주석 내부는 책풀이를 한 줄 조건문으로 옮긴 것
'''
def med3(a, b, c):
    if a >= b:
        #result = b if b>= c else c if a <= c else b
        if b >= c:
            return b
        elif a <= c:
            return c
        else:
            return b
    #else :
    #    result = a if a > c else c if b > c else b
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    #return result
'''


#### 1-3. 1부터 n까지 정수의 합 구하기
## 내풀이
def sum_to_n():
    n = int(input('n 값을 입력하세요.'))
    sum = 0
    for number in range(0, n+1):
        sum += number
    return sum

## 책풀이
'''
n = int(input('n값을 입력하세요.: '))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
'''
# 가우스 덧셈 활용
# sum = n * (n+1) // 2


#### 1-4. a 부터 b까지 정수의 합 구하기
## 내풀이
def sum_a_to_b():
    a, b = map(int, input('a, b값을 입력하세요.').split())
    if a > b : a, b = b, a
    sum = 0
    for number in range (a, b+1):
        sum += number
    return sum

## 책풀이
# 같은 방법


#### 1-5. +, - 번갈아 출력하기
## 내풀이
def print_plus_minus():
    n = int(input('출력 횟수를 정해주세요.'))
    if n % 2 == 0: result = '+-' * (n//2)
    else: result = '+-' * (n//2) + '+'
    return result

#### 1-6. *를 n개 출력하고, w개마다 줄바꾸기
## 내풀이 print문에서 실행하면 동작
def print_asterisk_breakline():
    n, w = map(int, input('*를 n개 출력하고 w개마다 줄바꿈합니다.').split())
    result = ('*'* w+'\n') * (n // w) + '*' * (n % w)
    return result