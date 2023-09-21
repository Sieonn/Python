# born_year = input("Born Year: ")
# print("age:", 2023 - int(born_year))


#input은 값을 받을때, 숫자 타입이 아니라 string으로 받는다.
#그래서 숫자로 전환해줘야한다.

# address = "서울시 강남구 역삼동"
# print(address[4:7])

# myString = "This is string"
# print(myString)
# print(type(myString))
# print(myString, "is of the data type", type(myString))

# firstString = "water"
# secondString = "fall"
# thirdStrinfg = firstString + secondString
# print(thirdStrinfg)

# name = input("What is your name?")
# print(name) 

# color = input("What is your favorite color?")
# animal = input("What is your favorite animal?")
# print("{},you like a {} {}!".format(name, color, animal))

tuple_ = ("banana", 50, 89.5, True)
#튜플은 수정 안됨.
# tuple_[3] = False
# 에러 발생
print(tuple_*3)
# print(tuple_ 3)