#local1.py

# b = 0
# print("b 값:",b)
# b = 1
# print("b 값:",b)


# def scope_test():
#     global a
#     a = 1
#     print("함수 내 a 값:",a)
    
# a = 0
# print("함수 밖 a 값:",a)
# scope_test()
# print("함수 호출 후 a 값:",a)


# def scope_test():
#     print("함수 내 a 값:",a)
#     a= 1
# a = 0
# print("함수 밖 a 값:",a)
# scope_test()
# print("함수 호출 후 a 값:",a)

b = 0
print("b 값:",b)
b = 1
print("b 값:",b)


def scope_test():
    a=0
    a = a+3
    print("함수 내 a 값:",a)
    return a
    
a = 0
print("함수 밖 a 값:",a)
a=scope_test()
print("함수 호출 후 a 값:",a)
