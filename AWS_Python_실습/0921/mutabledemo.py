# original = [1, 2, 3]
# target = original
# print(original, target)


# original = [1, 2, 3]
# target = original
# print(original, target)
# original[0] = 10000
# print(original, target) #originaldmf 바꿨더니 target이 바뀌었다. list, dict는 서로 연동되어있다. target은 original의 별칭이다라고 생각하면 쉽다.


import copy

original = [1, 2, 3]
# target = original
target = copy.deepcopy(original) #mutable 타입을  immutable type처럼 주소복사가 아니라 단순복사를 하는것. 반대는 shallowcopy이다.
print(original, target)
original[0] = 10000
print(original, target) #originaldmf 바꿨더니 target이 바뀌었다. list, dict는 서로 연동되어있다. target은 original의 별칭이다라고 생각하면 쉽다.
#component 요소