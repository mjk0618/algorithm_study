import random

n = int(input('몇 개의 숫자를 사용할지 입력하세요.'))
answer = random.sample(range(1, 10), n)
sblist = [None] * len(answer)
cnt = 0

print(f'정답 : {answer}') # 삭제

while True:
    while True:
        reply = list(map(int, input('정답을 입력하세요.').split()))
        if len(reply) == len(answer): break
        else: continue

    cnt += 1

    print(reply)

    for i in range(0, len(answer)):
        if reply[i] == answer[i]:
            sblist[i] = 'strike'
        elif reply[i] in answer:
            sblist[i] = 'ball'
        else: pass

    print(f'Strike: {sblist.count("strike")}\nBall: {sblist.count("ball")}')

    if sblist.count('strike') == len(answer):
        break

print(f'정답 : {answer}')
print(f'시도횟수 : {cnt}')
