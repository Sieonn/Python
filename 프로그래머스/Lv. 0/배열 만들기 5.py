def solution(intStrs, k, s, l):
    result = []
    for x in intStrs:
        if int(x[s:s+l]) > k:
            result.append(int(x[s:s+l]))           
    return result
    
intStrs = ["0123456789", "9876543210", "9999999999999"]
k = 50000
s = 5
l = 5
print(solution(intStrs, k, s, l))