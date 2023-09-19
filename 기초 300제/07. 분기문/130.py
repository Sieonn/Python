
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
if float(btc['opening_price']) + 변동폭 > float(btc['max_price']):
    print("상승장")
else:
    print("하락장")  

----------------------------------------------------------
[error]
import requests가  import되지 않았다.
그래서 cmd를 열어서 설정해줘야한다.
우선 경로를 재설정 해줘야한다.
pyhon이 설치된곳에 scripts파일에 들어가야한다.
C:\Python311\Scripts
C:\>cd \Python311\Scripts를 치고 Enter
그리고 pip install requests 하면 설치된다.
