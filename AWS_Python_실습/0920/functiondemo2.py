# original = 5
# target = original
# print('original = %d, target = %d'%(original, target))
# original = 100
# print(original,target)

def change(target):
    target = 100
    print('In the cange: target = %d'%target)

origin = 5
print("Before call change: origin = %d"%origin)
change(origin)
print("After call change: origin = %d"%origin)

# 숫자형(정수형, 실수형)과 문자열은 절대 바뀌지 않는다. => immutable type
# 수와 문자열은 immutable 타입