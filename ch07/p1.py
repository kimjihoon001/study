x = 10
def fadd(num):
    b = x+num
    print("변수x값은",x)
    print("변수b값은",b)
fadd(10)

# x = 10
# def fadd(num):
#     x = x+num
#     print("변수x값은",x)
# fadd(10)

x = 10
def fadd(num):
    global x
    x = x+num
    print("변수x값은",x)
fadd(10)
