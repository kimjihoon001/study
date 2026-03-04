# file_readlines.py

path = r"ch12\file1.txt"
f = open(path, 'r',encoding='utf-8')

lines = f.readlines()
# for line in lines:
#     print(line,end="")    
f.close()
