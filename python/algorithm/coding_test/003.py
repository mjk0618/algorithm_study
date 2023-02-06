#### 003. 구간 합 구하기1

## 내풀이
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(m):
    i, j = map(int, input().split())
    print(sum(numbers[i - 1: j]))

# 위와 같이 구현하면 시간초과가 발생한다.
# 따라서 구간합 배열을 미리 만들어놓아야 한다.

## 내풀이 수정
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])