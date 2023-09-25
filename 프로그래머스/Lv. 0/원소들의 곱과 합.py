# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, 
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9

# num_list = []
def solution(num_list):
    from math import prod
    if prod(num_list) < sum(num_list)**2 :
        return 1
    else:
        return 0
        