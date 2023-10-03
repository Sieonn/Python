def solution(x1, x2, x3, x4):
    answer = False
    if (x1+x2) and (x3+x4) >=1:
        answer = True
    elif (x1+x2) or (x3+x4) ==0:
        answer = False
    elif (x1+x2) and (x3+x4) ==0:
        answer = False
    return answer

#X V Y는 or연산
#X ^ Y는 and 연산 둘 다 참이여야지 T
# ----------------------------------------------------

def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)