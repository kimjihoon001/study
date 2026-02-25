# class 클래스명:
    #맴버 변수(=필드)
    #변수명 = 데이터값(속성값)
    
    #맴버 함수(=메서드)
    #def 함수명(매개변수,...):
        # 코드블록
        # self.변수명 = 데이터값
        # return 반환값
        
#객체 생성(생성자함수 사용)
#객체변수명 = 클래스()

#객체 접근
#객체변수명.변수명
#객체변수명.함수명(인수1,...) self는 제외


class 클래스명:
    pass

class Pizzacalss:
    def order(self):
        self.kind = 10
        print("주문하다.")
combo = Pizzacalss()
combo.order()
print(combo.kind)

potato=Pizzacalss()
potato.order()
print(potato.kind)