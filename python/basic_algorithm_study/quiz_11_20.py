#### 11. 모듈 사용 방법
# 1. sys 모듈 사용하기
'''
import sys
sys.path.append(current_working_directory)
import mymod
'''
# 2. PYTHONPATH 환경 변수 사용하기
'''
PYTHONPATH 환경 변수에 현재 디렉터리 지정 후 import
C:/Users/home> set PYTHONPATH=C:/doit
'''

# 3. 현재 디렉터리 사용하기
'''
현재 디렉터리에 mymo.py 위치시키고 import
'''


#### 12. 오류와 예외 처리
result = 0
try:
    [1,2,3][3]
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result) # 7 (한 줄 한 줄 순서대로 실행되므로 첫번째 에러인 IndexError 실행, 그리고 finally 실행)


#### 13. DashInsert 함수
data = '4546793'
def dash_insert(s : str) -> str:
    s = list(s)
    result = []
    for i in range(len(s)-1):
        result.append(s[i])
        if (int(s[i]) % 2 == 1) and (int(s[i + 1]) % 2 == 1):
            result.append('-')
        if (int(s[i]) % 2 == 0 ) and (int(s[i + 1]) % 2 == 0):
            result.append('*')
    result.append(s[-1])
    return result

## 책풀이
'''
def dash_insert_book(s):
    numbers = list(map(int, s))
    result = []

    for i, num in enumerate(numbers):
        result.append(str(num))
        if i < len(numbers) - 1:
            is_odd = num % 2 == 1
            is_next_odd = num % 2 == 1
            if is_odd and is_next_odd:
                result.append('-')
            elif not is_odd and not is_next_odd:
                result.append('*')
    return result
'''


#### 14. 문자열 압축하기
## 책풀이
def compress_string(s):
    _c = ''
    cnt = 0
    result = ''
    for c in s:
        if c != _c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress_string('aaabbcccccca'))

#### 15. Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

#### 16. 모스 부호
# 생략

#### 17. 기초 메타 문자
# 정규식 a[.]{3,}b과 매치되는 문자열
# 2. a....b

#### 18. 문자열 검색
import re
p = re.compile('[a-z]+')
m = p.search('5 python')
m.start() + m.end() # 10 / m.start == 2 / m.end == 8

#### 19. 그루핑"""
## 내풀이 (미완성)
phone = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
p_2 = re.compile('\d+[-]\d+[-](\d+)')
m_2 = p_2.sub('####', phone)

## 책풀이
pat = re.compile('(\d{3}[-]\d{4})[-]\d{4}') # 뒤의 숫자 4개를 변경할 것이므로 앞부분 그루핑
s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
result = pat.sub('\g<1>-####', s)
print(result)

#### 20. 전방 탐색
#p = re.compile('.*[.](?!com|net$).*$')

## 책풀이
pat_2 = re.compile('.*[@].*[.](?=com$|net$).*$')

print(pat_2.match('pahkey@gmail.com'))
print(pat_2.match('kim@daum.net'))
print(pat_2.match('lee@myhome.co.kr'))