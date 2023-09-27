# 문제 설명
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 
# 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

# 제한사항
# 1 ≤ l ≤ r ≤ 1,000,000
# 입출력 예
# l	r	result
# 5	555	[5, 50, 55, 500, 505, 550, 555]
# 10	20	[-1]


def solution(l, r):
    sd = []
    
    for i in range(l,r+1):
        if all(num in ['0','5'] for num in str(i)):
            sd.append(i)
            
    if len(sd) == 0:
        sd.append(-1)
        
    return sd   
                    
l = 5
r = 555
print(solution(l, r))

# a = 55
# b= str(a)
# print(int(b[1]))

