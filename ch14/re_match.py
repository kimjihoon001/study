# re_match.py

import re

p = re.compile('[^a-c]+')
print(p.match("python"))

print(p.match("3 python"))

print('---------')
p = re.compile('[a-z]+')
m = p.match("python")
if m:
    print(f"Match found: {m.group()}")
else:
    print('No match')
    
    
print(m.group())
print(m.span())
print(m.start())
print(m.end())

if m:
    print(f"Match found: {m.group()}")
else:
    print('No match')
    