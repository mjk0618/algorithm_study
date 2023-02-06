#### 002. 평균 구하기

## 내풀이
n = int(input())
score_list = list(map(int, input().split()))
m = max(score_list)
new_score_list = [i / m * 100 for i in score_list]
average = sum(new_score_list) / len(new_score_list)
print(average)

## 책풀이
""" 
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))
"""

# 변환 점수를 각 과목에 대하여 구할 필요 없이,
# 총합과 관련된 식으로 계산할 수 있다.
