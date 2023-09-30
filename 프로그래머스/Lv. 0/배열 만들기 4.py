def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if  len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.remove(stk[-1])
    return stk

arr = [1, 4, 2, 5, 3]

print(solution(arr))


# -----------------------------------------------

def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk