# clovers = ["클로버1","클로버2","클로버3"]

# for clover in clovers:
#     print(clover)

# for i in range(3):
#     print(clovers[i])

# count =1 
# while coint < 4:
#     count+=1
#     print(count)

# count = 0
# while count <= 5:
#     if count % 2 != 0:
#         print(count)
#     count+=1
# print(count)

# for i in range(101):
#     if i%3 ==0 and i!=0:
#         print(i)
        
# from itertools import combinations
# a="sca"
# b=sorted(a)
# print(b)
# h=[]
# for i in combinations(b,2):
#     h += i
# print(h)


# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i)

# number=int(input('총합을 구하려는 수를 입력하세요.'))
# result =0
# for i in range(number):
#     result += i+1
# print(f'1부터 {number} 까지의 총합은 {result} 이다.')

for a in range(1,6):
    for i in range(1,10):
        print(f"{a} x {i} = {a*i}") 