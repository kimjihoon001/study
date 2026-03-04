# raise1.py

try:
    raise NameError("hi there")
except NameError as e:
    print("An exception flew by!")
    print(e)