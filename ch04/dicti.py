# my_dict1= {}
# print(my_dict1)
# print(type(my_dict1))

# my_dict2={0:1, 1:2, 2:3}
# print(my_dict2)

# my_dict3={'이름':'엘리스','나이':10,'시력':[1.0,1.2]}
# print(my_dict3)
# my_dict3['이름']='보라'
# print(my_dict3)

# clover={'나이':27,'직업':'병사'}
# print(clover)
# clover['번호']=9
# print(clover)

# clover={'나이':{1:27,2:30,3:40},'직업':'병사','번호':9}
# print(clover['나이'][2])
# print(clover['번호'])
# clover['번호']=6
# print(clover['번호'])
# print(clover.get('번호'))

# muttable(뮤터블 가변객체)
# : 생성 후 내용을 변경할 수 있는 객체
# 같은 객체를 유지한 채, 내부 값이 변경
# ex) list, dict, set

# immutable(이뮤터블 불변객체)
# : 생성 후 내용을 변경할 수 없는 객체
# 값을 바꾸는 것처럼 보이지만 실제는 새 객체가 생성
# ex) int, float, str, tuple, bool


my_dict={'이름':'김지훈','나이':32,'성별':'남자','취미':{1:'게임',2:'운동',3:'영화감상'}}

my_dict['전화번호']='010-1234-5678'
my_dict['주소']='부산광역시 명장동'
my_dict['나이']+=1
print(my_dict)
print('--------')

print(my_dict.items())
for key, value in my_dict.items():
    print(key, ":", value)

print(type(my_dict.keys()))
print(type(my_dict.values()))