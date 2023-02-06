#### 5-3. 하노이의 탑
## 5-6. 하노이의 탑 구현하기
# 하노이 탑은 3가지 단계로 나타낼 수 있다.
# 우선 n개의 원반을 옮긴다고 할 때, 위에서부터 n-1개를 그룹으로 묶는다.
# 1. n-1개를 가운데 기둥으로 옮긴다. (재귀적으로 n-1개의 기둥을 옮긴다고 생각할 수 있다.)
# 2. 가장 큰 원반(n번째)을 마지막 기둥으로 옮긴다.
# 3. n-1개를 마지막 기둥으로 옮긴다. (마찬가지로 재귀적으로 n-1개의 기둥을 옮긴다고 생각할 수 있다.)
# 따라서 f(n-1) * 2 + 1번의 process가 필요하다 (점화식으로 풀면 일반항은 n^2 - 1임을 알 수 있다.)
# 원반이 1개 일때: 1번, 2개일 때: 3번, 3개일 때: 7번 ...

def move(no: int, x: int, y: int) -> None:
    """ 원반 no개를 x기둥에서 y기둥으로 옮김 """
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('하노이의 탑을 구현합니다.')
n = int(input('원반의 개수를 입력하세요.: '))
move(n, 1, 3) # 1기둥에 쌓인 원반 n개를 3기둥으로 옮김

#### 5-4. 8퀸 문제
# 8퀸 문제: 8개의 퀸이 서로 공격하여 잡을 수 없도록 8 x 8 체스판에 배치하세요. (92가지 해결 방법)
# 전체 경우의 수는 64 P 8 인데, 이걸 계산하는 건 불가능, 따라서 규칙을 세워 경우의 수를 줄인다.

# 규칙 1. 각 열에 퀸을 1개만 배치한다.
# 8^8 = 16,777,216 여전히 많다.

# 규칙 2. 각 행에 퀸을 1개만 배치한다.

## 5-7. 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기 (규칙 1 적용)
'''
pos = [0] * 8       # 각 열에서 퀸의 위치를 출력
def put() -> None:
    """ 각 열에 배치한 퀸의 위치를 출력 """
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """ i 열에 퀸을 배치 """
    for j in range(8):
        pos[i] = j      # 퀸을 j행에 배치
        if i == 7:      # 모든 열에 퀸 배치를 종료
            put()
        else:
            set(i + 1)  # 다음 열에 퀸을 배치

set(0)                  # 0열에 퀸을 배치
'''

## 5-8. 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기 (규칙 1, 2 적용)
'''
pos = [0] * 8                   # 각 열에서 퀸의 위치
flag = [False] * 8              # 각 행에 퀸을 배치했는지 체크

def put() -> None:
    """ 각 열에 배치한 퀸의 위치를 출력 """
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """ i열의 알맞은 위치에 퀸을 배치 """
    for j in range(8):
        if not flag[j]:         # j행에 퀸을 배치하지 않았으면
            pos[i] = j          # 퀸을 j행에 배치
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i + 1)      # 다음 열에 퀸을 배치
                flag[j] = False

set(0)                          # 0열에 퀸을 배치
'''

## 5-9. 8퀸 문제 알고리즘 구현하기

pos = [0] * 8               # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8        # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15       # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15       # 대각선 방향(↖↘)으로 퀸을 배치했는지 체크

def put() -> None:
    """ 각 열에 배치한 퀸의 위치를 출력 """
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def put_image() -> None:
    """ 퀸의 배치를 □과 ■로 출력 """
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    """ i열의 알맞은 위치에 퀸을 배치 """
    for j in range(8):
        if(     not flag_a[j]               # j행에 퀸이 배치되지 않았다면
            and not flag_b[i + j]           # 대각선 방향(↙↗)으로 퀸이 배치되지 않았다면
            and not flag_c[i - j + 7]):     # 대각선 방향(↖↘)으로 퀸이 배치되지 않았다면
            pos[i] = j                      # 퀸을 j행에 배치
            if i == 7:                      # 모든 열에 퀸을 배치 완료
                put_image()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)
