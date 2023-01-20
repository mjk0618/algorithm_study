#### 009. 슬라이딩 윈도우

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

# 새로 들어온 문자를 처리
def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 슬라이딩 윈도우가 이동하며 제거되는 문자 처리
def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# 조건이 0개 이상인 경우 미리 처리
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 최초 P 길이의 문자열 처리
for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

# 문자열 끝까지 이동하며 처리
for i in range(P, S):
    # 끝 index는 추가, 처음 index는 제거
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)