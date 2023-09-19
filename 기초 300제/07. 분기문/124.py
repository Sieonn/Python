# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# input number1: 10
# input number2: 9
# input number3: 20
# 20

users = []
for user in range(3): #실행할 수
	user = int(input("숫자를 입력하세요.: ")) #입력한 수의 타입은 string이여서 정수로 변환
	users.append(user) #순서대로 입력한 값들을 리스트에 저장
for i in range(3):
	print(f"input number{i+1}:", users[i])
print(max(users))

------------------------------------------------------
#other sol
user = input()
user = int(user)
user2 = input()
user2 = int(user2)
user3 = input()
user3 = int(user3)
list = [user, user2, user3]
print("input number1: ", user)
print("input number2: ", user2)
print("input number3: ", user3)
print(max(list))
