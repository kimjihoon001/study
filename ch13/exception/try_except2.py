# try_except2.py

# path=r"ch13\exception\myfile.txt"
# mode="w"

# f = open(path, mode)
# mode="r"
# f = open(path, mode)
# s = f.readline()
# i = int(s.strip())


# FileNotFoundError   읽을떄 없을때
# io.UnsupportedOperation "r"인데 write
# ValueError 문자열 숫자형으로 변환 할 떄
# print('---------------')
# path=r"myfile.txt"

# try:    
#     f = open(path)
#     s = f.readline()
#     i = int(s.strip())
# except FileNotFoundError:
#     print("파일을 찾을 수 없습니다.")

print('---------------')

path=r"ch13\myfile.txt"
mode="r"

try:    
    f = open(path,mode)
    s = f.readline()
    i = int(s.strip())
except (FileNotFoundError,ValueError):
    print("파일을 찾을 수 없습니다.")
except ValueError:
    print("정수형으로 변환 불가.")
# except Exception as err:
#     print("예외 발생!")
#     print(err)
finally:
    print("1")    
print("program exit")
