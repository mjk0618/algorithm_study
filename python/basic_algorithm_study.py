# 1-1  세 정수의 최댓값 구하기
'''
# 책풀이
def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum # 최댓값 반환

print(f'max(3, 2, 1) = {max3(3, 2, 1)}')

'''

''' 
# 내풀이
print('세 정수의 최댓값을 구합니다.')
a, b, c = map(int, input('세 정수를 입력하세요 :').split())

maximum = max([a,b,c])
print(f'최댓값은 "{maximum}"입니다.')
'''

