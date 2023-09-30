# 문제 설명
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# a, b, c, d는 1 이상 6 이하의 정수입니다.
# 입출력 예
# a	b	c	d	result
# 2	2	2	2	2222
# 4	1	4	4	1681
# 6	3	3	6	27
# 2	5	2	6	30
# 6	4	2	5


### 어려웠다,,,ㅠㅠㅠㅠ 다시 풀어보기

def solution(a,b,c,d):
    all_num = [a, b, c, d]
    counts = [all_num.count(i) for i in all_num]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) ==3:
        p = all_num[counts.index(3)]
        q = all_num[counts.index(1)]
        return (10*(p + q))**2
    elif max(counts) ==2:
        if min(counts) ==2: #이거는 두개씩 같은 수가 나왔을 때
            return (a + c) * abs(a - c) if a ==b else (a + b) * abs(a -b)
        #abs가 뭔지 공부하기어..? 설마 절대값인가 
        else: #두개가 같고 나머지 두 개는 다를때
            p = all_num[counts.index(2)]
            return (a*b*c*d)/ p**2
        # 만약에 같은 수를 a,b라고할때 p*p*c*d니까 나머지 값들의 곱을 구하려면 P*P로 나눠줘야한다.
    else:
        min(all_num)        


    
def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)
