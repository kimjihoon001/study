# re_option.py

import re


# 컴파일 옵션
# DOTALL, S

# p = re.compile('a.b',re.DOTALL)
# m = p.match('a\nb')
# print(m)

p = re.compile('a.b', re.S)
print(p.match('a\nb'))

print('----------------')


p = re.compile('[a-z]+')
m = p.match('Python')
print(m)

p = re.compile('[a-z]+', re.IGNORECASE)
print(p.match('Python'))

print('--------------')

p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

p = re.compile("^python\s\w+",re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

print('---------------')

p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

p = re.compile(r"""
&[#]
(
    0[0-7]+         #Octal form(8진수 형식)
    |[0-9]+         #Decimal form(10진수 형식)
    |x[0-9a-fA-F]+  #Hexadecimal form(16진수 형식)
)
;                   #후행 semicolon
""",re.VERBOSE    
)
data="&#07; &#8; &#x0A;"


print(p.findall(data))

