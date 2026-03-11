# class Node:
    
#     def __init__(self,key):
#         self.left = None
#         self.right = None
#         self.val = key
# class BST:
#     def __init__(self):
#         self.root=None
    
#     def insert(self,key):
        
#         if not self.root:
#             self.root = Node(key)
#         else:
#             curr = self.root
        
#         while True:
            
#             if key < curr.val:
#                 if curr.left:
#                     curr=curr.left
#                 else:
#                     curr.left = Node(key)
#                     break
                
#             else:
                
#                 if curr.right:
#                     curr=curr.right
#                 else:
#                     curr.right = Node(key)
#                     break
    
#     def search(self,key):
#         curr = self.root
        
#         while curr and curr != key:
            
#             if key<curr.val:
#                 curr = curr.left
#             else:
#                 curr=curr.right
#         return curr
    
#     def solution(lst,search_lst):
#         bst=BST()
        
#         for key in lst:
#             bst.insert(key)
#         result = []
        
#         for search_val in search_lst:
#             if bst.search(search_val):
#                 result.append("True")
#             else:
#                 result.append("False")
#         return result

# def total_sum(num):
#     count =0
#     for i in range(1,num+1):
#         count += i
#     return count


# class Phone:
#     def __init__(self,brand,year,color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#     def info(self):
#         print("제조사 :",self.brand)
#         print("출고년도 :",self.year)
#         print("색상 :",self.color)
#     def setinfo(self,brand,year,color):
#         self.brand = brand
#         self.year = year
#         self.color = color
        
# my_phone = Phone('samsung',2026,'white')
# my_phone.setinfo('iphone',2025,'black')
# my_phone.info()


# path="./pizza_file1.txt"
# mode="w"
# encoding="utf-8"

# with open(path,mode,encoding=encoding) as f:
#     f.write("페퍼로니피자 3000\n")
#     f.write("치즈피자 3200\n")
#     f.write("콤비네이션피자 3500\n")
    
# path="./pizza_file1.txt"
# mode="a"
# encoding="utf-8"

# with open(path,mode,encoding=encoding) as f:
#     f.write("불고기피자 3600\n")
#     f.write("해산물피자 3800\n")
    
# path="./pizza_file1.txt"
# mode="r"
# encoding="utf-8"

# with open(path,mode,encoding=encoding) as f:
#     pizza_readlines=f.readlines()
#     pizza=[]
#     for meun in pizza_readlines:
#         pizza.append(meun.split()[0])
# print(pizza)


# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     raise KeyError()
# except KeyError:
#     print("Key is missing!")


# add = lambda x,y : x+y
# print(add(3,5))

# per = ['10.31', "", "8.00"]
# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         print(0)


# numbers = [10, 20,30]

# try:
#     indexa=int(input("인덱스를 입력 하세요:"))
#     print(numbers[indexa])
# except IndexError:
#     print("잘못된인덱스입니다.")
# except ValueError:
#     print("잘못된 타입입니다.")    

# import re
# pattern = r'\w+'
# text = "Hello, World!"
# print(re.findall(pattern, text))

# import re
# pattern = r'(ab)+'
# text = "ababab"
# match = re.match(pattern, text)
# print(match.group())


# import re

# text="이메일목록: test@example.com, hello@world.net, user123@domain.org"
# print(re.findall(r'\w+@\w+.\w+',text))

# import re

# text = "연락처: 010-1234-5678, 02-987-6543, 031-456-7890"
# print(re.findall(r'\d+-\d+-\d+',text))

# import re

# text = "I love Python. Java is also popular. Python is great for AI"
# print(re.findall(r'[^.]*Python[^.]*', text))


# import re

# text = "상품코드: A123, B456, C789, 가격: 12000원"
# print(re.findall(r"[0-9]+",text))

# import re

# text = "NASA is working on AI projects with IBM and Google."
# print(re.findall(r"[A-Z]{2,}+",text))

# numbers = [1, 2, 3, 4, 5]
# iter_numbers = iter(numbers)

# for number in iter_numbers:
#     print(number)


# fruits = ["apple", "banana", "cherry"]

# it = iter(fruits)

# while True:
#     try:
#         item = next(it)
#         print(item)
#     except StopIteration:
#         break

# numbers = iter(range(0,10))
# for num in numbers:
#     if num%2==0 and num !=0:
#         print(num)

# class MyRange:
    
#     def __init__(self,start,stop,step):
#         self.start=start
#         self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         result = self.start
#         self.start += self.step
#         return result 

# for i in MyRange(2,10,2):
#     print(i)

# with open("data.txt",'w',encoding='utf-8') as file:
#     for i in range(1,11):
#         file.write(f"{i}번째 줄입니다.\n")
        
# print('파일이 성공적으로 작성되었습니다.')

# with open("data.txt",'a',encoding='utf-8') as file:
#     file.write("11번째 줄입니다.\n")

# with open("data.txt","r",encoding='utf-8') as file:
#     contents = file.read()
    
# print('파일내용:')
# print(contents)

# while True:
#     try:
#         number=int(input("숫자를 입력하세요:"))
#         print(number**2)
#         break
#     except ValueError:
#         print("올바른 숫자를 입력하세요!")

# print(list(map(lambda x: x**2,[10,20,30,40,50])))

# import re

# data = """python one
# life is too short
# python two
# you need python
# python three"""

# for result in re.findall(r'^python \w+',data,re.MULTILINE):
#     print(result)

# import re

# email= input("이메일을 입력하세요: ")

# p = re.compile(r"\w+@\w+\.\w+")

# m = re.match(p,email)

# if m:
#     print("올바른 이메일 형식입니다.")
# else:
#     print("잘못된 이메일 형식입니다.")


# def generatorfunc(stop):
#     start=1
#     while start <= stop:
#         yield start**2
#         start += 1

# n=5
# gfunc = generatorfunc(n)
# for _ in range(n):
#     print(next(gfunc))

# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self,x):
#         self.stack.append(x)
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return -1
#     def top(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             return -1


# def postfix_calc(expr):
#     stack = []
#     ops ={
#         '+': lambda a,b : a+b,
#         '-': lambda a,b : a-b,
#         '/': lambda a,b : a/b,
#         '*': lambda a,b : a*b
#     }
    
#     for token in expr.split():
        
#         if token in ops:
#             b = stack.pop()
#             a = stack.pop()
#             stack.append(ops[token](a,b))
#         else:
#             stack.append(int(token))
    
#     return stack.pop()

# print(postfix_calc("5 3 4 + -"))

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self,name):
#         self.queue.append(name)
        
#     def is_empty(self):
#         if len(self.queue) == 0:
#             return True
#         return False
    
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         return -1
    
#     def front(self):
#         if not self.is_empty():
#             return self.queue[0]
#         return -1
    
#     def status(self):
#         return self.queue
    
        
# bank = Queue()

# bank.enqueue("김철수")
# bank.enqueue("이영희")
# bank.enqueue("박민수")
# print(f"현재대기열: {bank.status()}")
# print(f"업무처리중인고객: {bank.dequeue()}")
# print(f"남은대기고객: {bank.status()}")



# class Deque:
#     def __init__(self):
#         self.deque = []
#     def push_front(self,x):
#         self.deque.insert(0,x)
#     def push_back(self,x):
#         self.deque.append(x)
#     def pop_front(self):
#         if not self.is_empty():
#             return self.deque.pop(0)
#         return -1
#     def pop_back(self):
#         if not self.is_empty():
#             return self.deque.pop()
#         return -1
#     def is_empty(self):
#         if len(self.deque) == 0:
#             return True
#         return False
# map1 = [
#     [0,1,1,1,1,1],
#     [0,1,0,0,0,1],
#     [0,1,0,1,0,1],
#     [0,1,0,1,0,0],
#     [0,0,0,1,1,0],
#     [1,1,1,1,1,0]
#     ]

# for map in map1:
#     print(map)
    
# rows, cols = map(int, input('행과 열을 입력하세요 ex)6 6:').split())

# map2 = []

# for _ in range(rows):
#     row = list(map(int, input('길 = 0, 벽 = 1을 입력하세요 ex)0 0 0 1 1:').split()))
#     map2.append(row)
    
# sx, sy = map(int, input("시작 좌표 입력 ex)0 0: ").split())

# if not (0 <= sx < rows and 0 <= sy < cols):
#     print("시작 좌표가 맵 밖입니다.")
#     exit()

# if map2[sx][sy] == 1:
#     print("시작 위치가 벽입니다.")
#     exit()

# def my_dfs(maps,start):
#     stack = []
#     visited = []
    
#     stack.append(start)
    
#     while stack:
#         r, c = stack.pop()
        
#         if (r,c) in visited:
#             continue
#         visited.append((r,c))
#         for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
#              nr, nc = r + dr, c + dc
#              if 0 <= nr < len(maps) and 0 <= nc <len(maps[0]):
#                 if (nr, nc) not in visited and maps[nr][nc] == 0:
#                     stack.append((nr,nc)) 
#     return visited

# print(my_dfs(map2, (sx, sy)))        


rows, cols = map(int, input('행과 열을 입력하세요 ex)6 6:').split())

map2 = []

for _ in range(rows):
    row = list(map(int, input('길 = 0, 벽 = 1을 입력하세요 ex)0 0 0 1 1:').split()))
    map2.append(row)
    
sx, sy = map(int, input("시작 좌표 입력 ex)0 0: ").split())

if not (0 <= sx < rows and 0 <= sy < cols):
    print("시작 좌표가 맵 밖입니다.")
    exit()

if map2[sx][sy] == 1:
    print("시작 위치가 벽입니다.")
    exit()

def my_bfs(maps,start):
    queue = []
    visited = []
    
    queue.append(start)
    
    while queue:
        r, c = queue.pop(0)
        
        if (r,c) in visited:
            continue
        visited.append((r,c))
        for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
             nr, nc = r + dr, c + dc
             if 0 <= nr < len(maps) and 0 <= nc <len(maps[0]):
                if (nr, nc) not in visited and maps[nr][nc] == 0:
                    queue.append((nr,nc)) 
    return visited

print(my_bfs(map2, (sx, sy)))        
                        
