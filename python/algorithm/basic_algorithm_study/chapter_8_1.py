#### 8-1. 연결 리스트
# 단순 배열로 구현한 연결 리스트는 데이터 삽입·삭제에 따라 데이터를 옮겨야 하므로 효율적이지 않다.

#### 8-2. 포인터를 이용한 연결 리스트
## 8-1. 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    """ 연결 리스트용 노드 클래스 """
    
    def __init__(self, data: Any = None, next: Node = None):
        """ 초기화 """
        self.data = data        # 데이터
        self.next = next        # 뒤쪽 포인터

class LinkedList:
    """ 연결 리스트 클래스 """
    
    def __init__(self) -> None:
        """ 초기화 """
        self.no = 0             # 노드의 개수
        self.head = None        # 머리 노드
        self.current = None     # 주목 노드

    def __len__(self) -> int:
        """ 연결 리스트의 노드 개수를 반환 """
        return self.no

    def search(self, data: Any) -> int:
        """ data와 값이 같은 노드를 검색 """
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        """ 연결 리스트에 data가 포함되어 있는지 확인 """
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """ 맨 앞에 노드를 삽입 """
        ptr = self.head         # 삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """ 맨 끝에 노드를 삽입 """
        if self.head is None:       # 리스트가 비어 있으면
            self.add_first(data)    # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        """ 머리 노드를 삭제 """
        if self.head is not None:   # 리스트가 비어있지 않으면
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        """ 꼬리 노드를 삭제 """
        if self.head is not None:   
            if self.head.next is None: # 노드가 1개 뿐이라면
                self.remove_first()
            else: 
                ptr = self.head         # 스캔 중인 노드
                pre = self.head         # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None         # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1
    
    def remove(self, p: Node) -> None:
        """ 노드 p를 삭제 """
        if self.head is not None:
            if p is self.head:          # p가 머리 노드이면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    def remove_current_node(self) -> None:
        """ 주목 노드를 삭제 """
        self.remove(self.current)

    def clear(self) -> None:
        """ 전체 노드를 삭제 """
        while self.head is not None:    # 전체가 비어 있을 때까지
            self.remove_first()         # 머리 노드를 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """ 주목 노드를 한 칸 뒤로 이동 """
        if self.current is None or self.current.next is None:
            return False                # 이동할 수 없음
        else:
            self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        """ 주목 노드를 출력 """
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """ 모든 노드를 출력 """
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        """ 이터레이터를 반환 """
        return LinkedListIterator(self.head)

class LinkedListIterator:
    """ 클래스 LinkedList의 이터레이터용 클래스 """

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

## 8-2. 포인터를 이용한 연결 리스트 클래스 LinkedList 사용하기
from enum import Enum

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제', '꼬리노드삭제', '주목노드출력', 
                     '주목노드이동', '주목노드삭제', '모든노드삭제', '검색', '멤버십판단', 
                     '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    """ 메뉴 선택 """
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='\n')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()                      # 연결 리스트를 생성

while True:
    menu = select_Menu()                # 메뉴를 선택

    if menu == Menu.머리에노드삽입:         # 맨 앞에 노드를 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:       # 맨 끝에 노드를 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:         # 맨 앞에 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:         # 맨 끝에 노드를 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:         # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:         # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:         # 주목 노드를 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:         # 모든 노드를 삭제
        lst.clear()

    elif menu == Menu.검색:                 # 노드를 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당하는 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:           # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
            +(' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else
                ' 있지 않습니다.'))
    
    elif menu == Menu.모든노드출력:         # 모든 노드를 출력
        lst.print()

    elif menu == Menu.스캔:                # 모든 노드를 스캔
        for e in lst:
            print(e)

    else:                                 # 종료
        break