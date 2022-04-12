import re

template = r'are you ready??.?.?'

input_str = input()
result = re.match(template, input_str)
print(len(result.group())) if result else print(0)
