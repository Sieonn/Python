def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        e = a + d*i
        if included[i]:
            sum += e
    return sum
#--------------------------------------------------------
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer
a = 3
b = 4
included = []