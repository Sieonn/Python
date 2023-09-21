#call by reference, mutable type
def change(target):
    target[0] = 10000
    print(f"In the change target = {target}")

original = [1, 2, 3]
print(f"Before change orignal = {original}")
change(original)
print(f"after change original = {original}")