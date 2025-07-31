class Calc:
    def getDivde(self, first_num, second_num):
        try:
            result = first_num / second_num
        except ZeroDivisionError:
            return "오류: 0으로 나눌 수 없습니다."
        except TypeError:
            return "오류: 숫자만 입력해야 합니다."
        else:
            return result

    def getZegop(self, a):
        return a*a

    def get_minus(self, num1: int, num2: int):
        return num1 - num2
    
    def getZegop(self, a):
        return a*a

    def getGopGop(self, param, param1, param2):
        return param * param1 * param2
    
    def getGop(self, a: int, b: int):
        return a * b
      
    def getZegop(self, a):
        return a*a
