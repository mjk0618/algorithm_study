#### 6-3. 단순 선택 정렬(straight selection sort)
# 아직 정렬하지 않은 부분에서 값이 가장 작은 원소 a[min]을 선택합니다.
# a[min]과 아직 정렬하지 않은 부분에서 맨 앞에 있는 원소를 교환합니다.
# n - 1번 반복

from typing import MutableSequence
## 6-6. 단순 선택 정렬 알고리즘 구현하기
def selection_sort(a: MutableSequence) -> None:
    """ 단순 선택 정렬 """
    n = len(a)
    for i in range(n - 1):
        min = i                         # 정렬할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]     # 정렬할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환

# 비교 횟수는 (n^2 - n) / 2 번이다
# 값이 같은 원소가 있어도 비교를 하고 순서를 바꾸므로 안정적이지 않은 정렬이다


#### 6-4. 단순 삽입 정렬(straight insertion sort)
## 6-7. 단순 삽입 정렬 알고리즘 구현하기
def insertion_sort(a: MutableSequence) -> None:
    """ 단순 삽입 정렬 """
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
'''
if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
'''

# 서로 떨어져 있는 원소를 교환하지 않는 안정적인 알고리즘, 원소 비교 횟수와 교횐 횟수 모두 n^2 / 2번\
# 셔틀 정렬(shuttle sort)이라고도 함

# 버블, 선택, 삽입의 단순 정렬 알고리즘은 모두 시간복잡도가 O(n^2)로 효율이 좋지 않음

## 6-8. 이진 삽입 정렬(binary insertion sort)
def binary_insertion_sort(a: MutableSequence) -> None:
    """ 이진 삽입 정렬 """
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0          # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1      # 검색 범위의 맨 뒤 원소 인덱스

        while True:
            pc = (pl + pr) // 2     # 검색 범위의 가운데 원소 인덱스
            if a[pc] == key:        # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1         # 검색 범위를 뒤쪽 절반으로 좁힘
            else:
                pr = pc - 1         # 검색 범위릘 앞쪽 절반으로 좁힘
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1     # 삽입해야 할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

## 6-9. 이진 삽입 정렬 알고리즘 구현(bisect.insort 사용)
import bisect

def binary_insertion_sort_2(a: MutableSequence) -> None:
    """ 이진 삽입 정렬(bisect.insort 사용) """
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)


if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = input(f'x[{i}]: ')

    binary_insertion_sort_2(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


