#### 001. 입력된 숫자의 합 구하기

## 내풀이
n = int(input())
test = list(input())
test = [int(i) for i in test]
answer = sum(test)
print(answer)

## 책풀이
'''
n = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum = sum + int(i)

print(sum)
'''