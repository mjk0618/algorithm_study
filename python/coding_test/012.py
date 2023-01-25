#### 012. 오큰수 구하기

N = int(input())
A = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(*answer)