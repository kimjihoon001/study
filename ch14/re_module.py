# re_module.py

import re

p = re.compile('[a-z]+')
m = p.match("python")
print(m)

# 매치객체 = re.match('정규표현식','검색대상문자열')

# 축약 후형태
m = re.match('[a-z]+',"python")
print(m)