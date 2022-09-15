# 1157
def _1157():
    word = input().upper()
    letter_dict = {}
    for s in word:
        if s not in letter_dict:
            letter_dict[s] = 1
        else:
            letter_dict[s] += 1
        if letter_dict[s] > (len(word) / 2):
            break

    cnt = 0
    for s in letter_dict:
        if letter_dict[s] == max(letter_dict.values()):
            cnt += 1
            result = s if cnt == 1 else '?'
    print(result)

# 1330
def _1330():
    a, b = map(int, input().split())
    result = '>' if a > b else '<' if a < b else '=='
    print(result)

# 1546
def _1546():
    n = int(input())
    score_list = list(map(int, input().split()))
    M = max(score_list)
    score_list = [i / M * 100 for i in score_list]
    avg = sum(score_list) / n
    print(avg)

# 2438
def _2438():
    n = int(input())
    i = 1
    while i <= n:
        print('*' * i)
        i += 1

# 2439
def _2439():
    n = int(input())
    i = 1
    s = '*'
    while i <= n:
        print(f'{s * i:>{n}}')
        i += 1

# 2475
def _2475():
    serial = list(map(int, input().split()))
    id = sum(list(map(lambda x: x ** 2, serial))) % 10
    print(id)

def _2562():
    num = [None] * 9
    for i in range(9):
        num[i] = int(input())
    maximum = (max(num), num.index(max(num)))
    print(maximum[0])
    print(maximum[1]+1)

def _2577():
    A = int(input())
    B = int(input())
    C = int(input())
    result = str(A * B * C)
    for i in range(0, 10):
        print(result.count(str(i)))

def _2675():
    T = int(input())
    S = []
    R = []
    for _ in range(T):
        a, b = map(str, input().split())
        S.append(int(a))
        R.append(b)

    for i in range(T):
        print(''.join([S[i] * s for s in R[i]]))

def _2739():
    n = int(input())
    for i in range(1, 10):
        print(f'{n} * {i} = {n * i}')

def _2741():
    n = int(input())
    for i in range(1, n + 1):
        print(i)

def _2742():
    n = int(input())
    for i in range(n, 0, -1):
        print(i)

def _2753():
    year = int(input())
    leap = 0
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        leap = 1
    else: leap = 0
    print(leap)

def _2884():
    h, m = map(int, input().split())
    m -= 45
    if m < 0:
        h -= 1
        m += 60
        if h < 0:
            h += 24
    print(h, m)

def _2908():
    a, b = map(str, input().split())
    a = list(a)
    a.reverse()
    b = list(b)
    b.reverse()
    a = int(''.join(a))
    b = int(''.join(b))
    print(a if a > b else b)

def _2920():
    s = list(input().split(' '))
    result = set([])
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            result.add('ascending')
        elif s[i] > s[i + 1]:
            result.add('descending')
    print(list(result)[0] if len(result) == 1 else 'mixed') 