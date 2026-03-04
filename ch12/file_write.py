# file_write.py

f = open("./ch12/file1.txt",'w',encoding='utf-8')    # raw
# f.write("hi\n",)
# f.write("thanks\n")
# f.write("welcome\n")
for i in range(1, 11):
    data = "%d 번쨰 줄입니다\n" % i
    f.write(data)
f.close()