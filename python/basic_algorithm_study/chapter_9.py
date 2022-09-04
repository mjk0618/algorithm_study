#### 9-1. 트리 구조
# 트리(tree)는 노드(node)와 가지(edge)로 구성
# 루트(root): 트리의 가장 위쪽에 있는 노드
# 리프(leaf): 가장 아래쪽에 있는 리프, 단말(terminal)/외부(external)노드라고도 함
# 리프를 제외한 노드(루트 포함)를 비단말 노드(non-terminal node)또는 내부(internal)노드라고 함
# 가지로 연결되었을 때 가장 위쪽에 있는 노드를 부모(parent), 아래쪽을 자식(child)라고 함, 부모가 같으면 형제(sibling)
# 가지를 위쪽으로 따라갈때 만나는 모든 노드를 조상(ancestor), 아래쪽을 자손(descendant)라고 함
# 루트에서 얼마나 멀리 떨어져 있는지를 레벨(level)로 표현, 최댓값은 높이(height)라고 함
# 각 노드가 갖는 자식의 수를 차수(degree)라고 함
# 루트의 자손으로 구성된 트리를 서브트리(subtree)라고 함
# 노드와 가지가 없는 트리를 빈 트리(None tree)또는 널 트리(null tree)라고 함

# 형제 노드의 순서가 있으면 순서 트리(ordered tree)없으면 무순서(unordered)트리

# 순서 트리의 검색
# 너비 우선 검색(breadth-first search): 가로 검색, 수평 검색
# 깊이 우선 검색(depth-first search): 세로 검색, 수직 검색

# 전위 순회(preorder): 노드 방문 -> 왼쪽 자식 -> 오른쪽 자식
# 중위 순회(inorder): 왼쪽 자식 -> 노드 방문 -> 오른쪽 자식
# 후위 순회(postorder): 왼쪽 자식 -> 오른쪽 자식 -> 노드 방문

#### 9-2. 이진 트리와 이진 검색 트리
# 노드가 왼쪽 자식과 오른쪽 자식만을 갖는 트리를 이진(binary)트리라고 한다.

## 완전 이진 트리(complete binary tree): 
# 마지막 레벨을 제외하고 모든 레벨에 노드가 가득 차 있고, 
# 마지막 레벨에 한해서 왼쪽부터 오른쪽으로 채우되 반드시 끝까지는 채우지 않아도 된다.

# 이진 검색트리의 조건
# 왼쪽 서브트리 노드의 키값은 자신의 노드 키값보다 작아야 한다
# 오른쪽 서브트리 노드의 키값은 자신의 노드 키값보다 커야 한다

## 9-1. 이진 검색 트리 구현하기
from __future__ import annotations
from typing import Any, Type

class Node:
    """ 이진 검색 트리의 노드 """
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """ 생성자(constructor) """
        self.key = key          # 키
        self.value = value      # 값
        self.left = left        # 왼쪽 포인터
        self.right = right      # 오른쪽 포인터

class BinarySearchTree:
    """ 이진 검색 트리 """
    def __init__(self):
        """ 초기화 """
        self.root = None            # 루트

    def search(self, key: Any) -> Any:
        """ 키가 key인 노드를 검색 """
        p = self.root               # p에 주목
        while True:
            if p is None:           # 더 이상 진행할 수 없다면
                return None         # 검색 실패
            if key == p.key:        # key와 노드 p의 키가 같으면
                return p.value      # 검색 성공
            elif key < p.key:       # key 쪽이 작으면
                p = p.left          # 왼쪽 서브트리에서 검색
            else:                   # key 쪽이 크면
                p = p.right         # 오른쪽 서브트리에서 검색

    def add(self, key: Any, value: Any) -> bool:
        """ 키가 key이고 값이 value인 노드를 삽입 """
        
        def add_node(node: Node, key: Any, value: Any) -> None:
            """ node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입 """
            if key == node.key:
                return False        # key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
            
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        """ 키가 key인 노드를 삭제 """  
        p = self.root                       # 스캔 중인 노드
        parent = None                       # 스캔 중인 노드의 부모 노드
        is_left_child = True                # p는 parent의 왼쪽 자식 노드인지 확인
        
        while True:
            if p is None:                   # 더 이상 진행할 수 없으면
                return False                # 그 키는 존재하지 않음

            if key == p.key:                # key와 노드 p의 키가 같으면
                break                       # 검색 성공
            else:
                parent = p                  # 가지를 내려가기 전에 부모를 설정
                if key < p.key:             # key쪽이 작으면
                    is_lef_child = True     # 여기서 내려가는 것은 왼쪽 자식
                    p = p.left              # 왼쪽 서브트리에거 검색
                else:
                    is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
                    p = p.right             # 오른쪽 서브트리에서 검색

        if p.left is None:                  # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:               # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent = p
            left = p.left                   # 서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key                # left의 키를 p로 이동
            p.value = left.value            # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left     # left를 삭제
            else:
                parent.right = left.left    # left를 삭제
        return True
            
    def dump(self, reverse = False) -> None:
        """ 덤프(모든 노드를 키의 오름차순으로 출력) """

        def print_subtree(node: Node):
            """ node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력 """
            if node is not None:
                print_subtree(node.left)    # 왼쪽 서브트리를 오름차순으로 출력
                print(f'{node.key}  {node.value}')  # node를 출력
                print_subtree(node.right)   # 오른쪽 서브트리를 오름차순으로 출력

        def print_subtree_rev(node: Node):
            """ node를 루트로 하는 서브트리의 노드를 키의 내림차순으로 출력 """
            if node is not None:
                print_subtree_rev(node.right)   # 오른쪽 서브트리를 내림차순으로 출력
                print(f'{node.key}  {node.value}') # 노드를 출력
                print_subtree_rev(node.left)    # 왼쪽 서브트리를 내림차순으로 출력

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)


    def min_key(self) -> Any:
        """ 가장 작은 키 """
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """ 가장 큰 키 """
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key


## 9-2. 이진 검색 트리 클래스 BinarySearchTree 사용하기
from enum import Enum

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    """ 메뉴 선택 """
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end ='\n')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()       # 이진 검색 트리를 생성

while True:
    menu = select_Menu()        # 메뉴 선택

    if menu == Menu.삽입:       # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:     # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.검색:     # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당하는 데이터가 없습니다.')
    
    elif menu == Menu.덤프:     # 덤프
        tree.dump()

    elif menu == Menu.키의범위: # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')

    else:                       # 종료
        break
    