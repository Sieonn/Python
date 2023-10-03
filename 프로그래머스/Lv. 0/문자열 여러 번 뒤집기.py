def solution(my_string, queries):
    for (s, e) in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]

#-----------------------------------------------


def solution(my_string, queries):
    result = list(my_string)
    for x, y in queries:
        result[x: y + 1] = reversed(result[x:y+1])
    return ''.join(result)


my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
print(solution(my_string, queries))
        