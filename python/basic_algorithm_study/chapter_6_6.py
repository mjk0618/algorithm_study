#### 6-8. 힙 정렬(heap sort)
# 힙은 부모의 값이 자식의 값보다 항상 크다(작다)는 조건을 만족하는 완전 이진 트리
# 힙에서 최댓값인 루트를 꺼내고, 루트 이외의 부분을 힙으로 만든다 -> 선택 정렬을 응용한 알고리즘

## 6-20. 힙 정렬 알고리즘 구현하기
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """ 힙 정렬 """

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """ a[left] ~ a[right]를 힙으로 만들기 """
        temp = a[left]          # 루트
        
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl         # 큰 값을 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):       # a[i] ~ a[n - 1]을 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]                 # 최댓값인 a[0]과 마지막 원소를 교환
        down_heap(a, 0, i - 1)                  # a[0] ~ a[i - 1]을 힙으로 만들기

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 단순 선택 정렬에서 최댓값인 원소를 선택하는 시간 복잡도는 O(n)이지만, 
# 힙 정렬에서 다시 힙으로 만드는 시간 복잡도는 O(log n)

# 단순 선택 정렬의 시간 복잡도는 O(n^2)이지만, 
# 힙 정렬은 원소의 개수만큼 작업을 반복하므로 O(n log n)으로 크게 줄어든다.

## 6-21. 힙 정렬 알고리즘 구현하기(heapq.push와 heapq.pop을 사용)
import heapq

def heap_sort_2(a: MutableSequence) -> None:
    """ 힙 정렬(heapq.push와 heapq.pop을 사용 """

    heap = []
    for i in a:
        heapq.heappush(heap, i)     # 힙에 원소를 추가 (힙의 조건을 유지)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)  # 힙에서 원소를 제거 (힙의 조건을 유지)

# (이하 생략)