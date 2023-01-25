#### 014. 절댓값 힙 구현하기

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
queue = PriorityQueue()

for i in range(N):
    num = int(input())
    if num == 0:
        if queue.empty():
            print("0\n")
        else:
            temp = queue.get()
            print(str(temp[1]) +'\n')
    else:
        queue.put((abs(num), num))