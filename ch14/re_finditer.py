# re_finditer.py
import re


# 반환형태: iterator object
p = re.compile('[a-z]+')
m = p.finditer("life is too short")

 
#  반환값 확인
# 1. 리스트 변환
# print(list(m))
# 2. for 문
# for 변수 in 리스트:

for match_obj in m:
    print(match_obj.group(),end=" ")
    print(match_obj.span())
 
 
print('------------')
    
print(list(p.finditer("3 python")))
# print(p.finditer("3py8thon"))

print('------------')

# text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
# p = re.compile('Python')
# m = p.finditer(text)
# print(m)


# p = re.compile('[a-z]*')
# print(p.finditer("pyt8hon"))

# 빈 문자열 ""도 매칭됨