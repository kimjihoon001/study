# slash.py

import re

# 패턴객체=re.compile("정규표현식")
# 패턴객체.match("검색대상문자열")

p = re.compile(r"\\section")
m=p.match("\section python hellow thanks")
print(m)

#   목적:   \section

# 1.  \s 화이트스페이스
# \\section

# 2.  파이썬 리터럴 규칙(이스케이프)
# "\\"=> "\"
# "\\\\"=>"\\"


##  raw string
# => 파이썬 문자열 리터럴 안에서
# \n, \t 같은 "이스케이프 코드 처리"를 없애주는 역활