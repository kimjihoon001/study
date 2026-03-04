# str_func.py

my_string="python is a popular programing language"
split_list = my_string.split()
print(split_list)
print(split_list[4])

# 문자열.strip()

my_string="\t     python is a popular programing language     \n"
print(my_string)
print(my_string.strip())

# 구분자.join(리스트)

my_list = ['apple', 'banana', 'cherry']
print(" ".join(my_list))
print(type(" ".join(my_list)))

my_list1=['123','456','789']
print(int("".join(my_list1)))
print(type(int("".join(my_list1))))