# def solution(n):
#     s = []
#     while n >= 1:
#         if n % 2 == 0:
#             n = n/2
#             s.append(n)
#             return n
#         else:
#             n = 3*n+1
#             s.append(n)
#             return n
#         if (n == 1): break
#     print(s)
def solution(n):
    s = []
    while n <= 1000:
        if n % 2 == 0:
            s.append(n)
            n //= 2
        else:
            s.append(n)
            n = 3*n + 1
        if (n == 1):
            s.append(n) 
            break
    return s

        # else:
        #     n = 3*n+1
        #     s.append(n)
n = 10
result = [10, 5, 16, 8, 4, 2, 1]

print(solution(n))