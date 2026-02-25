
# def 함수명(매개변수1,..2,):
#     코드블록
#     return 반환값

# 함수명(변수1,변수2,...)



# def personC(height, weight=1,age=10):
#     print("함수 기본값 없음")
#     print("나이",age,end=" ")
#     print("체중",weight,end=" ")
#     print("신장", height)
# personC(10,age=20,weight=10)   
# 1. 모든 매개변수에 기본값 설정 가능
# 2. 부분 매개변수에 기본값 설정시 뒤에서부터 설정할 것
# 3. 기본값이 있더라도 인수를 설정 가능(인수 우선 처리)
# 4. 인수 전달시 앞에서부터 설정 가능



# 키워드 인수 : 이름을 지정해서 전달하는 인수
# 위치 인수 : 순서대로 전달하는 인수
# print("hello")
# print("hello",end=" ")
# print("hello","toto",end=" ",sep="\n")

# 가변 위치 인수(*args): 갯수가 정해지지 않은 인수
# def total(*numbers):
#     print(numbers)
# total(1,"rla")

# # 가변 키워드 인자(**kwargs): 이름 붙은 인수를 여러개 받음
# def profile(**info):
#     print(info)
#     return list(info.items())
# a=profile(age=12,weight=11)
# print(a)

#전체 정리 예제
def example(a,b=10,*args,**kwargs):
    print("a: ",a)
    print("b: ",b)
    print("args: ",args)
    print("kwargs: ",kwargs)

example(1,2,3,4,x=100,y=200)

    
    