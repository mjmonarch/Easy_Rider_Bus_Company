import re

string = input()

template = r'\+(\d)[- ]?(\d{3})[- ]?([\d -]+)'
result = re.match(template, string, flags=re.DOTALL)

if result:
    print(f"Full number: {result.group(0)}")
    print(f"Country code: {result.group(1)}")
    print(f"Area code: {result.group(2)}")
    print(f"Number: {result.group(3)}")
else:
    print("No match")
