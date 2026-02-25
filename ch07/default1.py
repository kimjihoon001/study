
# def 함수명(매개변수1,..2,):
#     코드블록
#     return 반환값

# 함수명(변수1,변수2,...)

def persona(width, height):
    print("함수 기본값 없음")
    print("width=",width,end=" ")
    print("height", height)
def personb(width=4, height=3):
    print("함수 기본값 없음")
    print("width=",width,end=" ")
    print("height", height)

persona(10,20)
persona(30,40)
personb()
personb(50,60)
