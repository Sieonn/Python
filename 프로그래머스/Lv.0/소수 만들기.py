# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

def solution(nums): 
    make_nums = []
    reslut = []
    #만약 nums = [1, 2, 3, 4]
    # 123,124
    # 134,234
    for i in range(len(nums)-2): #len(nums) = 4개 그러므로 len(nums)-2는 2 i는 0, 1    |i = 0| i = 1
        for j in range(i+1, len(nums)-1): #start(0, 1),end 3 :: 0,1,2/ 1, 2 |j = 1 ,j = 2| j = 2
            for k in range(j+1, len(nums)):  #1, 2, /4 :: 1, 2, 3/ 2, 3 |k = 2, 3 , j = 3| k = 3
                make_nums.append(nums[i] + nums[j] + nums[k]) #make_nums = [6,7, 8, 9]
    for i in make_nums: #len(make_nums) = 4
      
      if all(i % j != 0 for j in range(2, i)): # i = 6,7,8,9 j = 2, 3 j가 0은 분모가 0이라 안되고, 1은 다 나눠져서 안됨.
          reslut.append(i) # i는 7 ,resulr = [7]
          
    return len(reslut) #:1개'



# --------------------------------------------------------------------------
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

nums = [1, 2, 3, 4]
print(solution(nums))
nums = [1, 2, 7, 6, 4]

print(solution(nums))