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


numbers = [10, 20,30]

try:
    indexa=int(input("인덱스를 입력 하세요:"))
    print(numbers[indexa])
except IndexError:
    print("잘못된인덱스입니다.")
except ValueError:
    print("잘못된 타입입니다.")    
    