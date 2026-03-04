# file_with.py

path=r"D:\rockey\py_work\ch12\file2.txt"
# mode1="w"


# with open(path,mode1,encoding="utf-8") as f:
#     f.write("No pain, no gain\n")
# mode2="a"
# with open(path,mode2,encoding="utf-8") as f:
#     f.write("노력 없이는, 얻는 것도 없다\n")
    
    
## 이스케이프(escape) 코드: 사전 정의된 문자 조합
# "\n" = new line
# "\t" = tab
# "\b" = backspace
# "\'" = 작은따옴표 표시
# "\"" = 큰따옴표 표시
# "\r" = 캐리지리턴(커서를 현재 줄의 가장 앞으로 이동)

print("hellow\t \"greet\" world!!",end="\n")
print("     \bthanks!",end="\r")
print('hi')