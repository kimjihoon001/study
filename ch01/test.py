# print('hello world')
# a=0
# print(id(a))
# a=1
# print(id(a))


# movie_rank = [' 하얼빈', '무파사:라이온킹', '소방관', '위키드']
# movie_rank.insert(3,'모아나 2')
# movie_rank.remove('소방관')
# print(movie_rank)

# nums=[1,2,3,4,5]
# result = 0
# for i in nums:
#     result += i
# print(result)


# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# count=0
# for _ in cook:
#     count += 1
# print(count)

# t = 1, 2, 3, 4
# print(type(t))

# t = ('a', 'b', 'c')
# t = ('A', 'B', 'C')
# print(t)

icecream = {"메로나": 1000,"폴라포": 1200,"빵빠레": 1800}
icecream['죠스바']=1200
icecream['월드콘']=1500
icecream['메로나']=1300
print('이름','희망가격',sep='\t')
for key,value in icecream.items():
    print(key, value, sep='\t')