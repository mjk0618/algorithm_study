answer = input()
blank = ["_" for _ in range(len(answer))]
cnt = 0

while True:
    reply = input()
    # 주어진 길이에 맞는 단어가 입력되었는지 확인
    if len(reply) != len(answer):
        continue
    else:
        cnt += 1
        reply = list(reply)
        for i in range(len(answer)):
            if answer[i] == reply[i]:
                blank[i] = answer[i]
    if '_' not in blank:
        break
    print(*blank, f"({cnt})")

print(f"answer: {''.join(blank)}")