def _1018(): pass
# 모든 가능한 8x8 체스판을 구하기 (set으로)
# 일렬로 정렬후 BW * 32 or WB * 32 string과의 차이를 구해서 최솟값 구하기

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

paint = 0

for i in range(len(board)):
    for j in range(len(i) - 1):
        if i[j] == i[j + 1]:
            paint += 1