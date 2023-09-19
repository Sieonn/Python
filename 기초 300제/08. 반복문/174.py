# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
T = 100
price_list = [32100, 32150, 32000, 32500]
for i in range(1, len(price_list)):
    T += 10
    print(T , price_list[i])
# ---------------------------------------------------------

price_list = [32100, 32150, 32000, 32500]
for i in range(1, len(price_list)):
    print(90 + i*10 , price_list[i ]) 