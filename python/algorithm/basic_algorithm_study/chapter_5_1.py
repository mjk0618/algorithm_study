#### 5-1. 재귀(recursion) 알고리즘 기본
## 5-1. 양의 정수 n의 팩토리얼 구하기
def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else: return 1
'''
if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)} 입니다.')
'''

## 5-2. 유클리드 호제법으로 최대 공약수 구하기
def gcd(x: int, y: int) -> int:
    """ 정숫값 x와 y의 최대 공약수를 반환 """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
'''
if __name__ == '__main__':
    print(f'두 정숫값의 최대 공약수를 구합니다.')
    x = int(input('첫 번째 정숫값을 입력하세요.: '))
    y = int(input('두 번째 정숫값을 입력하세요.: '))

    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)} 입니다.')
'''

#### 5-2. 재귀 알고리즘 분석
## 5-3. 순수한 재귀 함수 구현하기
def recur(n: int) -> int:
    """ 순수한 재귀 함수 recur의 구현 """
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

#x = int(input('정숫값을 입력하세요.: '))
#recur(x)

## 5-4. 비재귀적으로 재귀 함수 구현하기(꼬리 재귀를 제거)
def recur_2(n: int) -> int:
    """ 꼬리 재귀를 제거한 recur() 함수"""
    while n > 0: 
        recur(n - 1)
        print(n)
        n = n -2

## 5-5. 스택으로 재귀 함수 구현하기(재귀를 제거)
from chapter_4_1 import Stack

def recur_3(n: int) -> int:
    """ 재귀를 제거한 recur() 함수 """
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)           # n 값을 푸시
            n = n - 1
            continue
        if not s.is_empty():    # 스택이 비어 있지 않으면
            n = s.pop()         # 저장한 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정숫값을 입력하세요.: '))

recur(x)