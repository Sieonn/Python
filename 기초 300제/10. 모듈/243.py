# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 
# 전의 날짜를 화면에 출력해보세요.

from datetime import date, timedelta
오늘 = date.today()
for i in range(1,6):
    날짜 = 오늘 - timedelta(days= (6 - i))
    print(f"오늘부터 {6-i}일 전:",날짜)
