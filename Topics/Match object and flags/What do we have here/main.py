import re

template = r'... Jude'

input_str = input()

result = re.match(template, input_str)
print(result.group()) if result else print("None")