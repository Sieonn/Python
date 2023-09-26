# 문제 설명
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
# queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.

# 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.

# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ i < j < arr의 길이
# 입출력 예
# arr	queries	result
# [0, 1, 2, 3, 4]	[[0, 3],[1, 2],[1, 4]]	[3, 4, 1, 0, 2]

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
31204
32134
3413


# def solution(arr, queries):
 
#     # for i in arr:
#         for j in queries:
#             for k in range(1,len(j)):
#                 arr[j[k]] = arr[j[1-k]]
#         return arr
 
def solution(arr, queries):
    for s, e in queries:
        arr[s], arr[e] = arr[e], arr[s]
        
    return arr     

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
print(solution(arr,queries))
print([0,3][1])
print(arr)