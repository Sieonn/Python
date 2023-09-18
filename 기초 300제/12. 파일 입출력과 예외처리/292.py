바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.

005930 삼성전자
005380 현대차
035420 NAVER


f = open("F:\매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930", "삼성전자\n")
f.write("005380", "현대차\n")
f.write("035420", "Naver\n")
f.close()
