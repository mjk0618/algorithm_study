#### 8-4. 원형 이중 연결 리스트
# 원형 리스트(circulat list): 꼬리 노드가 다시 머리 노드를 가리키는 모양

# 이중 연결 리스트(doubly linked list)
# 연결 리스트의 단점은 뒤쪽 노드는 찾기 쉬운 반면 앞쪽 노드를 찾기 어렵다는 것인데
# 이를 개선하여, 뒤쪽 노드에 대한 포인터뿐만 아니라 앞쪽 노드에 대한 포인터가 주어진다

# 노드는 data, prev, next라는 3개의 필드로 구성된 클래스

# 위 둘을 결합한 것이 원형 이중 연결 리스트(circular doubly linked list)이다

## 8-5. 원형 이중 연결 리스트 구현하기
from __future__ import annotations
from typing import Any, Type

class Node:
    """ 원형 이중 연결 리스트용 노드 클래스 """

    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        """ 초기화 """
        self.data = data                # 데이터
        self.prev = prev or self        # 앞쪽 포인터
        self.next = next or self        # 뒤쪽 포인터

class DoubleLinkedList:
    """ 원형 이중 연결 리스트 클래스 """
    
    def __init__(self) -> None:
        self.head = self.current = Node()       # 더미 노드를 생성
        self.no = 0

    def __len(self) -> int:
        """ 연결 리스트의 노드 수를 반환 """
        return self.no

    def is_empty(self) -> bool:
        """ 리스트가 비었는지 확인 """
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """ data와 값이 같은 노드를 검색 """
        cnt = 0
        ptr = self.head.next            # 현재 스캔 중인 노드
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt              # 검색 성공
            cnt += 1
            ptr = ptr.next              # 뒤쪽 노드에 주목
        return -1                       # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """ 연결 리스트에 data가 포함되어 있는지 확인 """
        return self.serach(data) >= 0
    
    def print_current_node(self) -> None:
        """ 주목 노드를 출력 """
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)
     
    def print(self) -> None:
        """ 모든 노드를 출력 """
        ptr = self.head.next            # 더미 노드의 뒤쪽 노드 
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """ 모든 노드를 역순으로 출력 """
        ptr = self.head.prev            # 더미 노드의 앞쪽 노드
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """ 주목 노드를 한 칸 뒤로 이동 """
        if self.is_empty() or self.current.next is self.head:
            return False                # 이동할 수 없음
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """ 주목 노드를 한 칸 앞으로 이동 """
        if self.is_empty() or self.current.prev is self.head:
            return False                # 이동할 수 없음
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        """ 주목 노드 바로 뒤에 노드를 삽입 """
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """ 맨 앞에 노드를 삽입 """
        self.current = self.head        # 더미 노드 head의 바로 뒤에 삽입
        self.add(data)
    
    def add_last(self, data: Any) -> None:
        """ 맨 뒤에 노드를 삽입 """
        self.current = self.head.prev   # 꼬리 노드 head.prev의 바로 뒤에 삽입
        self.add(data)

    def remove_current_node(self) -> None:
        """ 주목 노드를 삭제 """
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """ 노드 p를 삭제 """
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:                   # p를 발견
                self.current = p
                self.remove_current_ndoe()
                break
            ptr = ptr.next
    
    def remove_first(self) -> None:
        """ 머리 노드를 삭제 """
        self.current = self.head.next       # 머리 노드 head.next를 삭제
        self.remove_current_node()

    def remove_last(self) -> None:
        """ 꼬리 노드를 삭제 """
        self.current = self.head.prev       # 꼬리 노드 head.prev를 삭제
        self.remove_current_node()

    def clear(self) -> None:
        """ 모든 노드를 삭제 """
        while not self.is_empty():          # 리스트 전체가 빌 때까지
            self.remove_first()             # 머리 노드를 삭제
        self.no = 0

    def __iter__(self) -> DoubleLinkedListIterator:
        """ 이터레이터를 반환 """
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListIterator:
        """ 내림차순 이터레이터를 반환 """
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    """ DoubleLinkedList의 이터레이터용 클래스 """

    def __init__(self, head: None):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    """ DoubleLinkedList의 내림차순 이터레이터 클래스 """
    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data


## 8-6. 원형 이중 연결 리스트 클래스 DoubleLinkedList 사용하기
from enum import Enum

Menu = Enum('메뉴', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입', '머리노드삭제', 
            '꼬리노드삭제', '주목노드출력', '주목노드이동', '주목노드역순이동', '주목노드삭제', 
            '모든노드삭제', '검색', '멤버십판단', '모든노드출력', '모든노드역순출력', 
            '모든노드스캔', '모든노드역순스캔', '종료'])

def select_Menu() -> Menu:
    """ 메뉴 선택 """
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='\n')
        n = int(input(' : '))
        if 1<= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()                # 원형 이중 연결 리스트를 생성

while True:
    menu = select_Menu()                # 메뉴 선택

    if menu == Menu.머리에노드삽입:         # 맨 앞에 노드를 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
    
    elif menu == Menu.꼬리에노드삽입:       # 맨 끝에 노드를 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.주목노드바로뒤삽입:   # 주목 노드 바로 뒤에 삽입
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:         # 맨 앞 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:         # 맨 끝 노드를 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:         # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:         # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드역순이동:     # 주목 노드를 한 칸 앞으로 이동
        lst.prev()
    
    elif menu == Menu.주목노드삭제:         # 주목 노드를 삭제
        lst.remove_current_node()
    
    elif menu == Menu.모든노드삭제:         # 모든 노드를 삭제
        lst.clear()

    elif menu == Menu.검색:                 # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:           # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
                +' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else '있지 않습니다.')

    elif menu == Menu.모든노드출력:         # 모든 노드를 출력
        lst.print()

    elif menu == Menu.모든노드역순출력:     # 모든 노드를 역순으로 출력
        lst.print_reverse()

    elif menu == Menu.모든노드스캔:         # 모든 노드를 스캔
        for e in lst:
            print(e)

    elif menu == Menu.모든노드역순스캔:     # 모든 노드를 역순으로 스캔
        for e in reversed(lst):
            print(e)

    else:                                 # 종료
        break

