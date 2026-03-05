# re_search.py

import re

p = re.compile('[a-z]+')
print(p.search("3 python"))

print('---------')
text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
p = re.compile('Python')
m = p.search(text)
print(m)

p = re.compile('[a-z]*')
m = p.search("3py8thon")
print(m)    #''
# 아무 것도 없어도 조건에 만족(0글자 매칭 가능)