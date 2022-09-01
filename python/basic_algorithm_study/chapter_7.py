# [7. 문자열 검색]
# 문자열 검색(string searching): 어떤 문자열 안에 다른 문자열이 포함되어 있는지를 검사하고 위치를 찾아내는 것
# 검색되는 문자열을 텍스트 찾아내는 문자열을 패턴이라고 함

#### 7-1. 브루트 포스법
## 이미 검사한 위치를 기억하지 못하므로 효율이 좋지 않다.

## 7-1. 브루트 포스법으로 문자열 검색하기
def bf_match(txt: str, pat: str) -> int:
    """ 브루트 포스법으로 문자열 검색 """
    pt = 0      # txt를 따라가는 순서
    pp = 0      # pat를 따라가는 순서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
    
    return pt - pp if pp == len(pat) else -1

'''
if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다.')
'''

## 멤버십 연산자(membership operator)와 표준 라이브러리를 사용한 문자열 검색
# ptn in txt, ptn not in txt
# str클래스의 find(), rfind(), index(), rindex() 함수
# with 계열 함수 startswith(), endswith()


#### 7-2. KMP법 (Knuth-Morris-Pratt법)
# 검사했던 결과를 버리지 않고 효율적으로 활용하는 알고리즘

## 7-2. KMP법으로 문자열 검색하기
def kmp_match(txt: str, pat: str) -> int:
    """ KMP 법으로 문자열 검색 """
    pt = 1                          # txt를 따라가는 커서
    pp = 0                          # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)     # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

'''
if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')
'''

# 텍스트를 스캔하는 커서 pt는 앞으로 나아갈 뿐 뒤로 돌아오지 않는다(브루트 포스법에는 없는 특징)
# 이 알고리즘은 복잡하고 실제 프로그램에는 별로 사용하지 않음


#### 7-3. 보이어·무어법(Boyer-Moor method)
# KMP법보다 효율적이어서 실제 문자열 검색에서 널리 사용하는 알고리즘

def bm_match(txt:str ,pat: str) -> int:
    """ 보이어·무어법으로 문자열 검색 """
    skip = [None] * 256     # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
            else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')
    s2 = input('패턴을 입력하세요.: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')

# 문자열 검색 알고리즘의 시간 복잡도(m = 패턴의 길이, n = 텍스트의 길이)
# 브루트 포스법 O(mn) :
# KMP법: O(n)
# 보이어무어법: 최악의 경우라도 O(n) 평균 O(n / m)

## 문자 코드를 다루는 ord()함수와 chr()함수
# ord()는 단일 문자를 받아 unicode 포인트를 정수로 반환
# ex) ord('a') = 97
# chr()은 이 과정을 역으로 수행
