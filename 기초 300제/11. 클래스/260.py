# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# class OMG :
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22>in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given

# -----------------------------------------------------------------------
class OMG:
    def print(self):
        print("oh my god")
myStock = OMG()
myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given
# 이거는 print()가 0개의 파라미터를 받아 실행하는데 1개가 주어졌다는 뜻이다.


# print()안에 self (또는 아무런 변수)를 넣으면 오류가 뜨지 않는다
# 이는 파이썬에서 객체자신이 인자로 들어가기 때문이다
# print()안에 파라미터가 없을시 위에서 mystock이 print()안의 파라미터로 들어가기 때문에
# 메서드에서 파라미터를 지정해주지 않았음에도 파라미터가 1개 들어갔다고 인식하게 된다.
# 그러므로 메서드안에 self(또는 아무런 변수)를 넣어서 파라미트가 무조건 들어올 객체를 받아줘야 한다.