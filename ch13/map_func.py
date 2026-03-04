# map_func.py

# def square(x):
#     return x**2

# numbers = [1,2,3,4,5]

# # # 이터레이터 = map(함수명, 이터러블)
# # squared_numbers = map(square, numbers)

# # # print(type(squared_numbers))
# # print(list(squared_numbers))
# # print(tuple(squared_numbers))

# squared_numbers = map(lambda x: x**2,numbers)
# print(list(squared_numbers))


print('-----------')

num_list = ['010', 1234, '5678']

joined_string = "-".join(map(str,num_list))
print(joined_string)