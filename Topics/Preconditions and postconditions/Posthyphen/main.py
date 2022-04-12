import re

string = input()
template = r'(?<=-)[a-z]+'

result = re.search(template, string)
print(result.group())
