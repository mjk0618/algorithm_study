#### 1. 문자열 바꾸기
s = 'a:b:c:d'
s = s.split(':')
s = '#'.join(s)
print(s)


#### 2. 딕셔너리 값 추출하기
a = {'A' : 90, 'B': 90}
if 'C' in a:
    print(a['C'])
else: 
    a.update(C = 70)
    print(a['C'])

## 책풀이 =>
a = {'A': 90, 'B': 80}
a.get('C', 70) # C라는 key가 있으면 value를 돌려주고 아니면 70이라는 값을 돌려줌

#### 3. 리스트의 더하기와 extend 함수
a = [1, 2, 3]
a += [4, 5]
a = [1, 2, 3]
a.extend([4, 5])

# a에 더한 것과 .extend를 한 것은 return 값이 다르다.
## 책풀이
# 리스트에 + 기호를 사용하여 더하면, 주소값이 달라져 새로운 리스트가 반환된다
# extend함수를 사용하면 주소 값(id)이 유지된다

#### 4. 리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = sum([i for i in A if i >= 50])
print(total)

## 책풀이
'''
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
'''

#### 5. 피보나치 함수:
def fibonacci(n):
    if n == 1 : return 0
    elif n == 2 : return 1
    else: return fibonacci(n-2) + fibonacci(n-1)

def fibonacci_list(n):
    list = [fibonacci(n) for n in range(1,n+1)]
    print(list)


#### 6. 숫자의 총합 구하기
num_list = []
n = int(input('입력할 숫자의 개수를 입력하세요. :'))
for _ in range(n):  
    num_list.append(int(input('숫자를 입력하세요. :')))
print(sum(num_list))

## 책풀이
'''
user_input = input('숫자를 입력하세요.: ')
numbers = user_input.split(',)
total = 0
for n in numbers:
    total += int(n)
print(total)
'''


#### 7. 한줄 구구단
gugu_n = 0
while gugu_n > 9 or gugu_n < 2 :
    gugu_n = int(input('구구단을 출력할 숫자를 입력하세요(2~9): '))
print([gugu_n * i for i in range(1,10)])



#### 8. 역순 저장
f = open('quiz8.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('quiz8.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()


#### 9. 평균값 구하기
f_9 = open('sample.txt', 'w')
score_list = [int(i) for i in f_9.readlines()]
avg = sum(score_list) / len(score_list)
f_9.write(f'\naverage: {avg}')
f.close()

## 책풀이
'''
f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)
f = open("result.txt", "w)
f.write(str(average))
f.close()
'''

#### 10. 사칙연산 계산기
class Calculator():
    def __init__(self, list):
        self.list = list

    def sum(self):
        return sum(self.list)

    def avg(self):
        return sum(self.list) / len(self.list)
        # return self.sum() / len(self.list)
