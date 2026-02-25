# def calculate_average(num_list):
#     total=0
#     for num in num_list:
#         total += num
#     average = total/len(num_list)
#     return average

# num_list = [10, 20, 30, 40, 50]
# average = calculate_average(num_list)
# print("평균: ", average)


# def check_odd_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_odd_even(4))  
# print(check_odd_even(7))  


my_dict={ 'a': 10, 'b': 20, 'c': 30 }

def add_sum(my_dict):
    total=0
    for num in my_dict.values():
        total += num
    return total

print(id(print(f"합은 {add_sum(my_dict)}")))