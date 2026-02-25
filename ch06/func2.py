# def fplusminus(arg):
#     if arg>0:
#         return str(arg)+" plus"
#     elif arg < 0:
#         return str(arg)+" minus"
#     elif arg==0:
#         return str(arg)+" zero"

# stra = fplusminus(0)
# print(stra)

# result1 = fplusminus(1)
# print(result1)

# result2 = fplusminus(-1)
# print(result2)


# print("------------")




# def myabs(arg):
#     if(arg<0):
#         result=arg*-1
#     else:
#         result=arg
#     return result

# myabs(10)


# def funca():
#     print("funca 함수 호출")
# def funcb():
#     funca()
#     print("funcb 함수 호출")
# def funcc():
#     funcb()
#     print("funcc 함수 호출")


# funcc()

# def fsub(pa,pb):
#     pc=pa-pb
#     return pc
# na=5
# nb=3
# nd=fsub(na,nb)
# print(f"{na} - {nb} = {nd}")

# def fadd(pa,pb):
#     pc=pa+pb
#     return pc
# def fsub(pa,pb):
#     pc=pa-pb
#     return pc
# def fmul(pa,pb):
#     pc=pa*pb
#     return pc
# def fdiv(pa,pb):
#     pc=pa/pb
#     return pc
# na = int(input("첫번쨰 숫자를 입력하세요 :"))
# nb = int(input("두번쨰 숫자를 입력하세요 :"))
# print(f"{na} + {nb} = {fadd(na,nb)}")
# print(f"{na} - {nb} = {fsub(na,nb)}")
# print(f"{na} * {nb} = {fmul(na,nb)}")
# print(f"{na} / {nb} = {fdiv(na,nb)}")

# sta="python example"

# def string_length(stb):
#     count = 0
#     for i in stb:
#         count +=1
#     return count
# lena=string_length(sta)
# print(lena)

# def fdiv(pa,pb):
#     if pb == 0:
#         print("0으로는 나눌수 없다")
#     else:
#         pc=pa/pb
#         print(f"{pa} / {pb} = {pc}")
      
# na=int(input("첫번쨰 숫자를 입력하세요 :"))
# nb=int(input("첫번쨰 숫자를 입력하세요 :"))

# fdiv(na,nb)

num = int(input("1부터 9까지 수 중 하나를 고르시오 :"))

def sum(pa):
    sum=0
    for i in range(0,101,pa):
        sum += i
    return sum

print(f"1부터 100까지의 {num}배수는 {sum(num)} 입니다.") 


