import re

s = 'a, b = 1'
# r = re.findall(r'(\w+-?)+', s)

# r = re.findall(r'(\w+-?)+', s)
#* 匹配a和b
r = re.findall(r'\s*(\w+)((?:,)\s*(\w+))*\s*=\s*\w*[^\)]', s)
print(r)
