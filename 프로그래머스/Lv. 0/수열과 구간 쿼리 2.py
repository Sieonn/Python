# 수열과 구간 쿼리 2
# 문제 설명
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
# queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

# 각 query마다 순서대로 s ≤ i ≤ e인 
# 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ s ≤ e < arr의 길이
# 0 ≤ k ≤ 1,000,000
# 입출력 예
# arr	queries	result
# [0, 1, 2, 4, 3]	[[0, 4, 2],[0, 3, 2],[0, 2, 2]]	[3, 4, -1]
# a[i] > k
# def solution(arr, queries):
    # re = []
    # so = []
    # # for i, j, v in queries:
    # #     for num in range(i, j+1): #0-4,0.1.2.3, 2
    # #         if arr[num] > v:
    # #             so.append(num)
            
    # #     # re.append(a)             
    # # else:
    # #     return so.append(-1)
    # # print(so)
    
    # # return re
    # for i, v, k in queries:
    #     for j in range():
        
            
           
# arr = [0, 1, 2, 4, 3]
# queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

# print(solution(arr, queries))
                


def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        lst = []
        for i in range(s, e + 1):
            if arr[i] > k:
                lst.append(arr[i])
        if len(lst) == 0:
            answer.append(-1)
        else:
            answer.append(min(lst))

    return answer

#아.. 설마  for a, b, c in queries면  1번 쿼리에 대해서 원소들을 나눠주는건가??
#a = 0 b = 4 c = 2같이..?
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(arr, queries))