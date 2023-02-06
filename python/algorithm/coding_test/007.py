#### 007. 주몽의 명령

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0
i = 0
j = N - 1
while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        answer += 1
        i += 1
        j -= 1

print(answer)