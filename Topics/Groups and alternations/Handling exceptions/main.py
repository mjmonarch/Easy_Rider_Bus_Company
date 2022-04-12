import re


# put your regex in the variable template
template = "(Value|Name|Type)Error"
string = input()
# compare the string and the template
result = re.match(template, string)
print(result.group(1)) if result else print("None")
