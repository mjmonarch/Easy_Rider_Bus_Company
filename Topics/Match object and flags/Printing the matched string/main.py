import re

template = "Good \w+"

string = input()
result = re.match(template, string)
print(result.group()) if result else print("No greeting!")
