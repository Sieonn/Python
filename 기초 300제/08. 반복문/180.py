# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, 
# low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000 ]

# 변동폭 = int(high_prices) - int(high_prices)
volatility = []
for i in range(5):
    변동폭 = int(high_prices[i]) - int(low_prices[i])
    volatility.append(변동폭)
print(volatility)