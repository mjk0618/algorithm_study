#### 6-5. 셸 정렬(shell sort)
# 단순 삽입 정렬의 장점은 살리고 단점은 보완하여 더 빠르게 정렬

## 6-10. 셀 정렬 알고리즘 구현하기
# 정렬 횟수는 늘어나지만 전체적으로 원소의 이동 횟수가 줄어들어 효율적임
from typing import MutableSequence
def shell_sort(a: MutableSequence) -> None:
    """ 셸 정렬 """
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

## 6-11. 셸 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)
def shell_sort_2(a: MutableSequence) -> None:
    """ 셸 정렬(h * 3 + 1의 수열 사용) """
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

'''
if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort_2(x)       # 배열 x를 셀 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
'''

# 셸 정렬의 시간 복잡도는 O(n^1.25), 단순 정렬은 O(n^2)
# 그러나 이웃하지 않고 떨어져 있는 원소를 교환하므로 안정적이지 않음

#### 6-6. 퀵 정렬(quick sort)
## 6-10. 배열을 두 그룹으로 나누기
def partition(a: MutableSequence) -> None:
    """ 배열을 나누어 출력 """
    n = len(a)
    pl = 0          # 왼쪽 커서
    pr = n - 1      # 오른쪽 커서
    x = a[n // 2]   # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl])               # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])      # a[pr + 1] ~ a[pl - 1]
    
    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])           # a[pr + 1] ~ a[n - 1]

'''
if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num                # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input('x[{i}]: '))

    partition(x)
'''

## 6-11. 퀵 정렬 알고리즘 구현하기
def qsort(a: MutableSequence, left: int, right: int) -> None:
    """ a[left] ~ a[right]를 퀵 정렬 """
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """ 퀵 정렬 """
    qsort_2(a, 0, len(a) - 1)

# 퀵 정렬은 서로 이웃하지 않는 원소를 교환하므로 안정적이지 않은 알고리즘

## 6-12. 퀵 정렬 알고리즘 구현하기(배열을 나누는 과정을 출력)
def qsort_verbose(a: MutableSequence, left: int, right: int) -> None:
    """ a[left] ~ a[right]를 퀵 정렬(배열을 나누는 과정 출력) """
    pl = left
    pr = right
    x =  a[(left + right) // 2]

    print(f'a[{left}] ~ a[{right}]:', *a[left : right + 1])

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort_verbose(a, left, pr)
    if pl < right: qsort_verbose(a, pl, right)

## 6-13. 비재귀적인 퀵 정렬 만들기
from chapter_4_1 import Stack

def qsort_2(a: MutableSequence, left: int, right: int) -> None:
    """ a[left] ~ a[right]를 퀵 정렬(비재귀적인 퀵 정렬) """
    range = Stack(right - left + 1)     # 스택 생성

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()      # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2]              # 피벗(가운데 원소)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 꺼냄
        if pl < right: range.push(pl, right)    # 오른쪽 그룹의 커서를 꺼냄

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num        # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
