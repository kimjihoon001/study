# re_findall.py
import re

p = re.compile('[a-z]+')
m = p.findall("life is too short")
print(m)
print(p.findall("3 python"))
print(p.findall("3py8thon"))

print('------------')

text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
p = re.compile('Python')
m = p.findall(text)
print(m)


p = re.compile('[a-z]*')
print(p.findall("pyt8hon"))

# 빈 문자열 ""도 매칭됨