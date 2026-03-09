food = ['김밥', '만두', '양념치킨', '족발', '피자', '쫄면', '라면']
food_iter=iter(food)
# for i in food_iter:
#     print(i)
# print(next(food_iter))  # StopIteration

# # 이터레이터 생성방법
# 1. iter() 함수 활용
# 2. 클래스 작성
# 3. 제너레이터 생성

# print('__iter__' in dir(food_iter))
# print('__next__' in dir(food_iter))
# print(hasattr(food_iter,'__iter__'))
# print(hasattr(food_iter,'__next__'))



# # 제너레이터 생성 방법
# 1. yield
# 2. 제너레이터 컴프리핸션
# 3. 클래스

def write_file(file_path):
    with open(file_path,'w',encoding='utf-8') as file:
        for data in food_iter:
            file.write(data)
            file.write('\n')
path=r'ch15\project2.txt'

write_file(path)

def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        for line in file.readlines():
            yield line.strip()

liens= read_file(path)
print(next(liens))

# 파일 자체도 이터레이터임
