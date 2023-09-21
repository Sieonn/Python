student = {}

def my_input(man):
    name = input("Enter your name:")
    age = input("Enter your age:")
    man["name"] = name
    man["age"] = age
    

my_input(student)
print(student)