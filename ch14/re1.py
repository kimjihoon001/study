# re1.py
# 정규표현식(Regular Expression)
# : 문자열 패턴 정의해서
# 검색, 검사, 치환, 추출 등을 할 수 있게 해주는
# 문자열 처리 규칙

import re

# 정규표현식을 정의해서 컴파일 함수 인자로 전달하면
# 패턴 객체를 반환 함.
# 패턴객체: "검색대상문자열"에서 패턴의 발견을 도와주는 객체

# 패턴객체 = re.compile("정규표현식")
# 매치객체=패턴객체.match("검색대상문자열")
# print(매치객체)
# match 함수 : 문자열 처음부터 정규식과 매치되는지 조사함

# 메타 문자: 별도의 의미가 담겨있는 문자
# p = re.compile("[a]")
# n = p.match("banana")
# print(n)

# p = re.compile("[a]")
# n = p.match("apple")
# print(n)

# p = re.compile("[ab]")  #b or a
# print(p.match("apple"))
# print(p.match("banana"))

# p = re.compile("[abc]")
# print(p.match("a"))
# print(p.match("before"))
# print(p.match("dude"))

# print('-------------')

# p = re.compile("[a-c]")
# print(p.match("a"))
# print(p.match("dude"))

# print('-------------')

# p = re.compile("[ab][ab]")
# print(p.match("banana"))
# print(p.match("apple"))

# print('-------------')

# p = re.compile("ba")    # 2 letter 매치 여부
# print(p.match("banana"))
# print(p.match("apple"))

# print('-------------')

p = re.compile("[^0-5]")
print(p.match("6banana"))
print(p.match("banana"))
print(p.match("^banana"))

# print('-------------')

# p = re.compile("[\^0\-5]")
# print(p.match("6banana"))
# print(p.match("banana"))
# print(p.match("^banana"))
# print('-------------')

# p = re.compile("[a-zA-z]")
# print(p.match("banana"))
# print(p.match("apple"))
# print(p.match("Apple"))

# print('-------------')
# p = re.compile("\d")
# print(p.match("1banana"))
# print(p.match("apple"))
# print(p.match("Apple"))

# print('-------------')
# p = re.compile("\D")
# print(p.match("1banana"))
# print(p.match("apple"))
# print(p.match("Apple"))


# print('-------------')
# p = re.compile("\w")
# print(p.match("1banana"))
# print(p.match("apple"))
# print(p.match("Apple"))


# print('-------------')
# p = re.compile("\W")
# print(p.match("1banana"))
# print(p.match("apple"))
# print(p.match("Apple"))


# # 정규표현식의 문자범위는
# # 아스키코드 순서로 범위를 계산


# print('-------------')
# p = re.compile("\s")
# # p = re.compile(" \t\n\r\f\v")
# # p = re.compile("\S")
# # p = re.compile("^ \t\n\r\f\v")
# print(p.match("apple"))
# print(p.match(" apple"))
# print(p.match("\tApple"))
# print(p.match("\nApple"))


# print('-------------')
# # .(dot) 문자

# p = re.compile("..")
# print(p.match("apple"))


# p = re.compile("a.b")
# print(p.match("aab"))
# print(p.match("a0b"))
# print(p.match("abc"))
# print(p.match("a\nb"))
# print(p.match("a\tb"))

# print('-------------')
# p = re.compile("a[.]b")
# print(p.match("aab"))
# print(p.match("a.b"))


# print('-------------')
# p = re.compile("ca*t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))


# print('-------------')
# p = re.compile("ca+t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))


# print('-------------')
# # {} 문자
# # {m,n}
# # {m}

# p = re.compile("ca{2,}t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaat"))


# p = re.compile("ca{,5}t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaaaaat"))

# p = re.compile("ca{2,4}t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaaaat"))


# print('-------------')
# p = re.compile("ca{,}t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaaaaat"))


# print('-------------')
# # p = re.compile("ca{0,1}t")
# p = re.compile("ca?t")
# print(p.match("ct"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaaaaat"))

# print('-------------')
# # ^문자
# p = re.compile("^hello")
# print(p.match("hello"))
# print(p.match("cat"))
# print(p.match("caat"))
# print(p.match("caaaaaat"))


# print('-------------')
# # $문자
# p = re.compile("hello$")
# print(p.match("hello, world"))
# print(p.match("world, hello"))
# print(p.match("kim,hello,kenneth,hello"))
# print(p.match("hello"))

# print('-------------')
# # $문자
# # search 함수: 문자열 전체에서 일치 여부 검색
# # 일치하는 첫번째 문자열 변환

# p = re.compile("hello$")
# print(p.search("hello, world"))
# print(p.search("world, hello"))
# print(p.search("kim,hello,kenneth,hello"))
# print(p.search("hello"))