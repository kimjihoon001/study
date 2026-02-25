
# def 함수명(매개1, 매개2):
    # 코드블록
    # return 반환값
na = 10
nb = 11  
def swap_func(pa,pb):
    temp = pa
    pa = pb 
    pb = temp
    return pa,pb


print('na=',na,'nb=',nb)

na,nb =swap_func(na,nb)
print('na=',na,'nb=',nb)
