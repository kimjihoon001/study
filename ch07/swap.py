#swqp.py

# 변수간 데이터 스왑1
na=10
nb=11
print('na=',na,'nb=',nb)

temp = na
na = nb
nb = temp
print('na=',na,'nb=',nb)

print('------------------')
na=10
nb=11
print('na=',na,'nb=',nb)
na, nb=nb, na
print('na=',na,'nb=',nb)