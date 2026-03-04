# string1.py

muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type(muna))
try:
    muna[0]='k'
except TypeError as e:
    print(type(e),e)
    


munb = ["python"]
print(munb[0])
print(type(munb))

munc=["p","y","t","h","o","n"]
print(munc[0])
print(munc[1])
print(munc[2])
print(type(munc))
munc[0]='k'
print(munc)

print('---------------')

for i in range(0,6,1):
    print(munc[i])
        
print('---------------')

print(hex(ord('a')))
print(ord('A'))

print(chr(0x61))
print(chr(0x41))

print(ord('가'))



### 다양한 문자열 사용(출력) 방법
# 표준 출력 함수: print(함수) 활용
# 1. 기능 : 인수를 모니터 출력
# 2. 인수: 객체(다양한 자료형 모두)
# 3. 리턴값: 없음(None)

# 기본 형식
name="홍길동"
age=18
print("이름:", name, "나이:", age)

# 1. % 연산자 사용 방식
# 서식 문자 활용 => %s: 문자열, %d:10진수, %f:실수형, %x:16진수
print("이름: %s 나이: %d"%(name,age))

# 2. format()메서드 사용 방식
print("이름 {} 나이: {}".format(name, age))

# 3. f-string 사용 방식
print(f"이름: {name} 나이: {age}")