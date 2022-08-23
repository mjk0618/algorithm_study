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

#### 7. 정규 표현식
# 문자 클래스 [] -> [] 사이의 문자들과 매치
#    ex) [abc] a: match, before: match, dude: not match
# 문자 클래스 내부의 ^는 반대라는 의미
# \d 숫자와 매치, \D 숫자가 아닌 것과 매치
# \s whitespace와 매치 [\t\n\r\f\v], \S whitespace가 아닌 것과 매치
# \w 문자+숫자와 매치 [a-zA-Z0-9], \W 문자+숫자가 아닌것과 매치

# Dot(.) -> \n을 제외한 모든 문자와 매치
#   ex) a.b aab: match, a0b: match, abc: not match
#   cf) a[.]b는 a와 b사이에 .이 있어야 match라는 뜻

# * 반복
#   ex) ca*t: *앞에 있는 a가 '0번' 이상 반복되면 매치
#   ex) ct: match, cat: match
# + 반복
#   ex) ca+t: +앞에 있는 a가 최소 '1번' 이상 반복되면 매치
#   ex) ct: not match, cat: match
# {m,n},? 반복
#   ex) ca{2}t: a가 2번 반복되면 매치
#   ex) ca{2,5}t: a가 2~5번 반복되면 매치
#   ex) ab?c: b가 0~1번 사용되면 매치 (있거나 없거나)


def practice_regex():
    import re # 정규 표현식을 지원하는 모듈
    #p = re.comple('ab*') # a뒤에 b가오고 b가 0번 이상 반복되면 매치

    ## 컴파일된 패턴 객체의 메서드
    # match(): 문자열의 처음부터 정규식과 매치되는지 조사
    # search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사
    # findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려줌
    # finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려줌

    # match
    p = re.compile('[a-z]+') # 정규식 [a-z]중 아무거나 1번 이상 반복
    m = p.match('python') # 모든 index가 a-z에 포함
    print(m) # <re.Match object; span=(0, 6), match='python'> 

    m_2 = p.match('3 python') # 문자열의 시작이 정규식과 match x
    print(m_2) # None 리턴

    # search
    s = p.search('python')
    print(s) # <re.Match object; span=(0, 6), match='python'>

    s_2 = p.search('3 python') # search는 문자열 전체에 대해서 조사하므로 return값이 존재
    print(s_2) # <re.Match object; span=(2, 8), match='python'>

    result = p.findall("life is too short") # 리스트로 return
    print(result) # ['life', 'is', 'too', 'short']

    result_2 = p.finditer("life is too short")
    print(result_2) # <callable_iterator object at 0x000001F84B04FB80>

    for r in result_2: print(r)
    # <re.Match object; span=(0, 4), match='life'>
    # <re.Match object; span=(5, 7), match='is'>
    # <re.Match object; span=(8, 11), match='too'>
    # <re.Match object; span=(12, 17), match='short'>

    ## match 객체의 메서드
    # gorup(): 매치된 문자열을 돌려줌
    # start(): 매치된 문자열의 시작 위치를 돌려줌
    # end(): 매치된 문자의 끝 위치를 돌려줌
    # span(): 매치된 문자의 (시작, 끝)에 해당하는 튜플을 돌려줌

    # m = p.match('python')
    m.group() # 'python'
    m.start() # 0
    m.end() # 6
    m.span() # (0,6)

    # -> search()를 했다면 '3 python'에 대하여
    # 'python', 2, 8, (2,8) return


    ## 컴파일 옵션
    # DOTALL (S): dot 문자(.)가 줄바꿈 문자를 포함하여 모든 문자와 매치
    # IGNORECASE (I): 대,소문자 구분하지 않고 매치
    # MULTILINE (M): 여러 줄과 매치
    # VERBOSE (X): verbose모드를 사용

    # DOTALL 예시
    p_3 = re.compile('a.b')
    m_3 = p_3.match('a\nb')
    print(m_3) # None

    p_4 = re.compile('a.b', re.DOTALL) # = re.S
    m_4 = p_4.match('a\nb')
    print(m_4) # <re.Match object; span=(0, 3), match='a\nb'>

    # IGNORECASE 예시
    p_5 = re.compile('[a-z]', re.I) # = re.IGNORECASE
    p_5.match('python') # <re.Match object; span=(0, 1), match='p'>
    p_5.match('Python') # <re.Match object; span=(0, 1), match='P'>
    p_5.match('PYTHON') # <re.Match object; span=(0, 1), match='P'>

    # MULTILINE 예시
    p_6 = re.compile('^python\s\w+') # ^python:으로 시작 하면서, \s: whitespace가 있고, \w+: 숫자 또는 문자가 1개 이상 반복
    data = """python one
    life is too short
    python two
    you need python
    python three"""

    print(p_6.findall(data)) # ['python one']

    p_7 = re.compile('^python\s\w+', re.MULTILINE) # 각 라인의 첫번째 줄에 정규식 적용
    print(p_7.findall(data)) # ['python one', 'python two', 'python three']

    # VERBOSE 예시
    charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

    charref = re.compile(r"""
    &[#]                # Start of a numeric entitiy reference)
    (
        0[0-7]+         # Octal form
        |[0-9]+         # Decimal form
        |x[0-9a-fA-F]   # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """, re.VERBOSE)

    # 첫번째, 두번째 식 같은 의미, 하지만 보기 쉽고 주석을 달 수 있음


    ## 백슬래시 문제
    # \section 문자열을 찾으려고 하지만,
    # [\t\b\n\r\f\v]ection 으로 인식
    # \\section 또는 rstring 사용

    ## 메타문자
    # | (or)
    p_8 = re.compile('Crow|Servo')
    m_8 = p_8.match('CrowHello')
    print(m_8) # <re.Match object; span=(0, 4), match='Crow'>

    # ^ (문자열의 맨 처음) 
    print(re.search('^Life', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
    print(re.search('^Life', 'My Life')) # None

    # $ (문자열의 끝)
    print(re.search('short$', 'Life is too short')) # <re.Match object; span=(12, 17), match='short'>
    print(re.search('short$', 'Life is too short, you need python')) # None

    # \A 문자열의 처음
    # ^와 같지만, re.MULTILINE옵션에서의 차이가 발생
    # ^는 각 줄의 문자열의 처음, \A는 줄과 상관없이 전체 문자열의 처음

    # \Z 문자열의 끝 (\A와 같은 원리)

    # \b 단어 구분자(word boundary)
    p_9 = re.compile(r'\bclass\b')
    print(p_9.search('no class at all')) # <re.Match object; span=(3, 8), match='class'>
    print(p_9.search('the declassified algorithm')) # None 앞 뒤가 whitespace가 아니므로 match x

    # \B \b와 반대로 whitespace로 구분되지 않은 경우만 매치

    ## 그루핑
    # ex) (ABC)+: ABC가 1번 이상 반복되는지 조사
    p_10 = re.compile('(ABC)+')
    m_10 = p_10.search('ABCABCABC OK?')
    print(m_10) # <re.Match object; span=(0, 9), match='ABCABCABC'>
    print(m_10.group(0)) # ABCABCABC

    p_11 = re.compile(r'\w+\s+\d+[-]\d+[-]\d+') 
    # \w+: 문자/숫자가 1개 이상, \s+: whitespace가 1개 이상, \d+: 숫자가 1개 이상, [-]: -문자 존재, \d+ 숫자가 1개 이상
    m_11 = p_11.search('park 010-1234-1234')
    # \w+ -> park, \s+ -> 공백, \d+ -> 010, [-] -> -, \d+ -> 1234, [-] -> -, \d+ -> 1234

    p_12 = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+') #(\w+)로 그루핑, group 메서드에서 그루핑된 부분의 문자열만 추출 가능
    # group(0): 매치된 전체 문자열
    # group(1): 첫 번째 그룹에 해당하는 문자열
    # group(n): n 번째 그룹에 해당하는 문자열
    m_12 = p_12.search('park 010-1234-1234')
    print(m_12.group(1)) # park

    p_13 = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)') # 두번째 그룹을 전화번호 부분으로 지정
    print(p_13.search('park 010-1234-1234').group(2)) # 010-1234-1234


    # 그룹에 이름 붙이기
    # (\w+) -> (?P<name>\w+)로 바꾸면됨

    p_14 = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
    m_14 = p_14.search('park 010-1234-1234')
    print(m_14.group('name')) # park
    print(m_14.group('phone')) # 010-1234-1234


## 전방 탐색(Lookahead Assertions)
import re
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group()) # http:

# 긍정형 전방 탐색(positive)
# (?=...) ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 소비: 검색에 포함되어 검색 결과에 포함됨
# 소비되지 않음: 검색에 포함되지만 검색 결과에는 포함되지 않음
p = re.compile('.+(?=:)')
m = p.search("http://google.com")
print(m.group()) # http

# 부정형 전방 탐색(negative)
# (?!...) ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# .*[.](?!bat$).*$  -> .bat로 끝나지 않으면 매치
# .*[.](?!bat$|exe$).*$ -> .bat, .exe로 끝나지 않으면 매치

## 문자열 바꾸기 sub 메서드 사용
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes') # 'colour socks and colour shoes'
    # 바꿀 문자열, 대상 문자열

p.sub('colour', 'blue socks and red shoes', count = 1) # 'colour socks and red shoes' 1번만 바꿈
p.subn('colour', 'blue socks and red shoes', count = 1) # ('colour socks and red shoes', 1) 결과를 튜플로 반환

# sub메서드에서 참조 구문 사용하기
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub('\g<phone> \g<name>', "park 010-1234-1234")) # 010-1234-1234 park

# sub메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.') 
# 'Call 0xffd2 for printing, 0xc000 for user code.'

## Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
len(s) # 32
print(re.match('<.*>', s).span()) #(0, 32) -> Greedy, 매치할 수 있는 최대한의 문자열을 소비
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>


print(re.match('<.*?>', s).group()) # <html> -> Non-Greedy, 가능한 한 최소한의 반복을 수행