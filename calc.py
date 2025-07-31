class Calc:
    # 이곳에 코드를 작성
    pass

    def getDivde(self, first_num, second_num):
        try:
            result = first_num / second_num
        except ZeroDivisionError:
            return "오류: 0으로 나눌 수 없습니다."
        except TypeError:
            return "오류: 숫자만 입력해야 합니다."
        else:
            return result