# file_add.py

f = open("./ch12/file1.txt",'a',encoding='utf-8')    # raw
# f.write("hi\n",)
# f.write("thanks\n")
# f.write("welcome\n")
for i in range(11, 21):
    data = "%d 번쨰 줄입니다\n" % i
    f.write(data)
    
f.close()