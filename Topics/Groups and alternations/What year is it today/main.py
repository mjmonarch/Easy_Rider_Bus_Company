import re


# put your regex in the variable template
template = "(\d{1,2})[/\.](\d{1,2})[/\.](\d{4})"
string = input()

result = re.match(template, string)
print(result.group(3)) if result else print("None")
