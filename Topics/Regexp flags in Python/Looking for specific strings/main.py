import re

string = input()
template = '^b.*l$'

result = re.search(template, string, flags=re.IGNORECASE|re.DOTALL)
print(result.group()) if result else print("No match")