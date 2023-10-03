def solution(number):
    nums = []
    for i in number:
        nums.append(int(i))
    return sum(nums) % 9
        
number = "1234526"
print(solution(number))