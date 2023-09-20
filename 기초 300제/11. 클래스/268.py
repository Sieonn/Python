# PER, PBR, 배당수익률은 변경될 수 있는 값입니다.
# 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.
class Stock:
    def __init__(self, name, code, PER, PBR, divi):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.divi = divi
        
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)