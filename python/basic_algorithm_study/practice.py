#1.
'''
class Calculator:
    def __init__(self):
       self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
'''

#2.
'''
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100: self.value = 100

cal = MaxLimitCalculator()
'''

#3. 3과 5의 배수 합하기
def three_multiple(n :int):
    multiples = [i for i in range(1, n+1) if (i % 3 == 0)]
    result = sum(multiples)
    return result, multiples
    
def five_multiple(n :int):
    multiples = [i for i in range(1, n+1) if (i % 5 == 0)]
    result = sum(multiples)
    return result, multiples

def sum_multiples(n: int):
    result = three_multiple(n)[0] + five_multiple(n)[0]
    return result

#4. 게시판 페이징하기
def getTotalpage(m: int, n: int) -> int:
    pages = m // n if (m % n == 0) else (m // n) + 1
    return pages

#5. 탭을 4개의 공백으로 바꾸기
def change_tabsize(s: str):
    result = s.replace("\t", " " * 4)
    return result

#6. 하위 디렉터리 검색하기
def search_dir(dir: str):
    import os
    files = os.listdir(dir)
    for file in files:
        full_filename = os.path.join(dir, file)
        print(full_filename)


# 코딩 연습 사이트
# https://projecteuler.net/archives