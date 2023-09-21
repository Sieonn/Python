# # 문제 설명
# # 문자열 code가 주어집니다.
# # code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

# # mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

# # --여기서부터 집중!-
# # mode가 0일 때
# # code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# # code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# # mode가 1일 때
# # code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# # code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
# # 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

# # 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.
# def solution(code):
#     mode = True
#     ret = ""
#     for i in range(len(code)) and :        
#         if mode == 0:
#             if code[i] == "1":
#                 mode = 1
#                 return mode
#             else:
#                 if i%2== 0:
#                     ret += ret + code[i]
#                 return ret   
#         else:
#             if code[i] == "1":
#                 return mode
#             else:
#                 if 1%2==1:
#                      ret += ret + code[i]
#                 return ret 

# code = "abc1abc1abc"
# print(solution(code))            

def solution(code):
    mode = True
    ret = ""
    for i , v in enumerate(code): #enumerate 하면 인덱스와 값이 주어진다.
        if mode: #mode = 0
            if v != "1" and i % 2 ==0:
                ret = ret + v
            elif v == "1":
                mode = False
        else:
            if v != '1' and i % 2 == 1:
                ret = ret +v
            elif v == '1':
                mode = True
                
    if len(ret) == 0:
        return 'empty'
    return ret
                
code = "abc1abc1abc"
print(solution(code))    

                
                
                
                     
             