'''
바이트 페어 인코딩(BPE)란?
데이터에서 가장 많이 등장한 문자열을 병합해서 데이터를 압축하는 기법
(a, b, c, d)라는 초기 사전으로 구성된 aaabdaaabac 라는 문자열이 있다고 한다. 
연속된 두 글자를 한 글자로 병합한다고 하면, 가장 많이 나타난 aa를 Z로 병합할 수 있다.
ZabdZabac
여기서 또 ab가 가장 많이 나타났으므로 Y로 병합하면 다음과 같다.
ZYdZYac
ZY는 다시 한번 X로 병합할 수 있으므로 최종 결과는 다음과 같다.
XdXac
사전 크기는 (a, b, c, d, Z, Y, X)로 7개가 되고 데이터 길이는 11에서 5로 줄어든다.
'''

# n >= 10, m >= 4라고 하자.

import random

# 문자열의 길이와 초기 사전의 크기 지정
n = int(input())
m = int(input())
word_dict = [chr(97 + i) for i in range(m)]

# 테스트 케이스(s) 생성
def creat_test_case(n):
    s = ""
    for i in range(n):
        s += word_dict[random.randrange(0, len(word_dict))]
    return s

s = "adcdacdbcd"

# s에 대하여 BPE 적용
word_cnt = dict()
for i in range(len(s)-1):
    word_cnt[s[i:i+2]] = 0


#### 미완성 ####
## word_cnt 딕셔너리 먼저 완성하기
## 더 좋은 압축 알고리즘이 있는지 구상하기