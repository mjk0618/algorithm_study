#### 2-1. 학생 5명의 점수를 입력받아 합계와 평균을 구하기
## 내풀이
def student_scores():
    scores = list(map(int, input('학생 5명의 점수를 입력하세요.').split()))
    sum_scores = sum(scores)
    avg = sum_scores / len(scores)
    return sum_scores, avg


#### 2-2. 시퀀스 원소의 최댓값 출력하기
## 책풀이
from typing import Any, Sequence
def max_of(a: Sequence) -> Any:
    """ 시퀀스형 a 원소의 최댓값을 반환 """
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

'''
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
    
    print(f'최댓값은 {max_of(x)}입니다.')
'''

#### 2-3. 배열 원소의 최댓값을 구해서 출력하기(난수)
def max_of_sequence():
    import random

    num, low, high = map(int, input('배열의 원소 수, 난수의 최소, 최댓값을 입력하세요.').split())
    number_list = [None] * num
    for i in range(num):
        number_list[i] = random.randint(low, high)

    return number_list, max_of(number_list)


#### 2-4. 배열을 역순으로 저장하기
## 내풀이
def reversed_array(a: list):
    for i in range(len(a) // 2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    return a

## 책풀이
'''
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i -1] = a[n - i -1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input('fx[{i}]값을 입력하세요.: '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')2
'''

#### 2-5. 10진수를 2~36진수로 변환하기
## 내풀이(10진수까지만 가능)
def base_conversion(n :int, base: int):
    new_n = []
    while(n > 0):
        new_n.append(str(n % base))
        n = n // base
    new_n.reverse()
    new_n = ''.join(new_n)
    return new_n

## 책풀이
def card_conv(x:int, r:int) -> str:
    ''' 정수 x를 r진수로 변환한 뒤 문자열로 반환 '''
    d = '' # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

#### 2-6. 소수 구하기(n까지)
## 내풀이
def is_prime(n: int):
    counter = 0
    prime_list = []
    for i in range(2, n+1):
        for j in range(2, i):
            counter += 1
            if(i % j == 0): break
        else: prime_list.append(i)      
    return prime_list, counter

## 책풀이 1000까지의 소수
'''
counter = 0
for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0: break
    else: print(n)
print(counter)
'''

#### 2-7. 소수 구하기(소수 리스트 활용)
## 내풀이 (처음)
def is_prime2(n: int):
    counter = 0
    prime_list = [2]
    for i in range(2, n+1):
        for j in prime_list:
            counter += 1
            if(i % j == 0): break
        else: prime_list.append(i)
    return prime_list, counter

## 내풀이 (수정)
def is_prime2_2(n: int):
    counter = 0
    prime_list = [2]
    for i in range(3, n+1, 2):
        for j in prime_list[1:]:
            counter += 1
            if(i % j == 0): break
        else: prime_list.append(i)
    return prime_list, counter

## 책풀이
'''counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0: break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(counter)
'''

#### 2-8. 소수 구하기 (소인수 크기의 성질 활용)
## 내풀이 (처음)
def is_prime3(n: int):
    counter = 0
    prime_list = [2]
    for i in range(3, n+1, 2):
        for j in prime_list:
            counter += 2
            if j * j > i:
                break
        end = prime_list.index(j)
        start = end - 1
        for k in prime_list[:end]:
            counter += 1
            if i % k == 0: break
        else: prime_list.append(i)
    return prime_list, counter

## 책풀이
'''
counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print([prime[i]])
print(counter)
'''

## 내풀이 (수정)
def is_prime3_2(n: int):
    counter = 0
    prime_list = [2, 3]
    for i in range(5, n+1, 2): # 같음
        for j in prime_list[1:]:
            if j * j > i:
                break
            counter += 2
        end = prime_list.index(j)
        for k in prime_list[:end]:
            if i % k == 0: break
            counter += 1
        else: prime_list.append(i)
    return prime_list, counter