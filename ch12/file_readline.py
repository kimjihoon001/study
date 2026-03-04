# file_readline.py

path = r"ch12\file1.txt"
f = open(path, 'r',encoding='utf-8')

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)
f.close()
