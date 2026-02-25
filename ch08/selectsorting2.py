# ca = [21,10,11,15,13]
# mina=ca[0]
# minix=0
# for sb in range(1,5,1):
#     if mina > ca[sb]:
#         mina=ca[sb]
#         minix=sb

# temp=ca[0]
# ca[0]=ca[minix]
# ca[minix]=temp
# print(ca)

# print('----------------')

# mina=ca[1]
# minix=1
# for sb in range(2,5,1):
#     if mina > ca[sb]:
#         mina=ca[sb]
#         minix=sb
# temp=ca[1]
# ca[1]=ca[minix]
# ca[minix]=temp
# print(ca)

# print('----------------')

# mina=ca[2]
# minix=2
# for sb in range(3,5,1):
#     if mina > ca[sb]:
#         mina=ca[sb]
#         minix=sb
# temp=ca[2]
# ca[2]=ca[minix]
# ca[minix]=temp
# print(ca)

# print('----------------')

# mina=ca[3]
# minix=3
# for sb in range(4,5,1):
#     if mina > ca[sb]:
#         mina=ca[sb]
#         minix=sb
# temp=ca[3]
# ca[3]=ca[minix]
# ca[minix]=temp
# print(ca)

print('----------------')


# ca = [21,10,11,15,13]

# for i in range(4):
#     mina=ca[i]
#     minix=i
#     for sb in range(i+1,5,1):
#         if mina > ca[sb]:
#             mina=ca[sb]
#             minix=sb
#     temp=ca[i]
#     ca[i]=ca[minix]
#     ca[minix]=temp
#     print(ca)    

ca = [21,10,11,15,13]

def fselsort(ca):
    for i in range(len(ca)-1):
        mina=ca[i]
        minix=i
        for j in range(i+1,len(ca),1):
            if mina > ca[j]:
                mina=ca[j]
                minix=j
        temp=ca[i]
        ca[i]=ca[minix]
        ca[minix]=temp  
    return ca
print(fselsort(ca))
