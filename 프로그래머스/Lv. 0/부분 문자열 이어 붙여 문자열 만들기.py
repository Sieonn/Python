# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
# 1 ≤ my_strings의 원소의 길이 ≤ 100
# parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
# 0 ≤ s ≤ e < my_strings[i]의 길이
# 입출력 예
# my_strings	parts	result
# ["progressive", "hamburger", "hammer", "ahocorasick"]	[[0, 4], [1, 2], [3, 5], [7, 7]]	"programmers"

def solution(my_string, parts):
    set = []
    for i in range(len(my_string)):
        x = parts[i][0]
        y = parts[i][1]
        set.append(my_string[i][x : y+1])
    return ''.join(set)

        

    # return ''.join(set)

my_string = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts =  [[0, 4], [1, 2], [3, 5], [7, 7]]

print(solution(my_string, parts))

# -----------------------------------------------------------------------------
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])
# ------------------------------

2
3
4
5
6
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer