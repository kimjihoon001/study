a = [10,11,12,13]

print("리스트 a 값",a)

print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))


a[1]=21
print("리스트 a 값",a)
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))

b=a
print("리스트 b 값",b)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))

b[2]=42
print("리스트 a 값",a)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))
b=[30,31,32,33]

print("리스트 b 값",b)
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[2]))
print(id(b[3]))
