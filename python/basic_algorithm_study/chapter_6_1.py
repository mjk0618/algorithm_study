#### 6-1. 정렬 알고리즘
# 안정적인(stable) 알고리즘
# 내부(internal) 정렬, 외부(external) 정렬

#### 6-2. 버블 정렬 (Bubble sort)
# 이웃한 두 원소이 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘, 단순 교환 정렬
## 6-1. 버블 정렬 알고리즘 구현하기
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """ 버블 정렬 """
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):            # 패스를 n - 1번 수행
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

# 원소를 비교하는 횟수는 (n-1)+(n-2) + ... + 1 = n(n-1)/2
# 그러나 실제 원소를 교환하는 횟수는 배열의 원솟값에 따라 영향을 받으므로 평균값은 n(n-1)/4

## 6-2. 버블 정렬 알고리즘 구현하기(정렬 과정을 출력)
def bubble_sort_verbose(a: MutableSequence) -> None:
    """ 버블 정렬 (정렬 과정을 출력) """
    ccnt = 0    # 비교 횟수
    scnt = 0    # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f'[패스 {i + 1}]')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j -1 else 
                                     ' +' if a[j -1] > a[j] else ' -'), 
                                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

## 6-3. 버블 정렬 알고리즘 구현하기(알고리즘 개선 1)
def bubble_sort_improved_1(a: MutableSequence) -> None:
    """ 버블 정렬 (교환 횟수에 따른 중단) """
    ccnt = 0    # 비교 횟수
    scnt = 0    # 교환 횟수

    n = len(a)
    for i in range(n - 1):
        print(f'[패스 {i + 1}]')
        exchng = 0  # 페스에서 교환 횟수
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j -1 else 
                                     ' +' if a[j -1] > a[j] else ' -'), 
                                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break

        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

## 6-4. 버블 정렬 알고리즘 구현하기(알고리즘 개선2)
def bubble_sort_improved_2(a: MutableSequence) -> None:
    """ 버블 정렬(스캔 범위를 제한) """
    ccnt = 0    # 비교 횟수
    scnt = 0    # 교환 횟수
    n = len(a)
    k = 0
    i = 0
    while k < n - 1:
        print(f'[패스 {i + 1}]')
        i += 1
        last = n - 1
        for j in range(n - 1, k, - 1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j -1 else 
                                     ' +' if a[j -1] > a[j] else ' -'), 
                                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

## 6-5. 셰이커 정렬(shaker sort) 알고리즘 구현하기
# 양방향(bidirectional) 버블 정렬, 칵테일(cocktail) 정렬, 칵테일 셰이커 정렬
def shaker_sort(a: MutableSequence) -> None:
    """ 셰이커 정렬 """
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'패스{i + 1}')
        i += 1
        for j in range(right, left, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')

        if (left == right):
             break
        print(f'패스 {i + 1}')
        i += 1
        for j in range(left, right):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j else
                                    ' +' if a[j] > a[j + 1] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                             # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)                               # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')