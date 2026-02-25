
count=0
while count<3:
    count += 1
    if count==2:
        continue
    print(count)
    
count=0
while count<3:
    count += 1
    if count==2:
        break
    print(count)
    
for j in range(5):
    for i in range(10):
        print("*",end="")
    print()
    
print("***********")
print("***********")
print("***********")
print("***********")
print("***********")
for i in [1,2,3,4,5]:
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("*",end="")
    print("\n")
    
    
for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5,6,7,8,9,10]:
        print('*',end="")
    print(end="\n")
    