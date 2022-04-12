import re

password = input()

template = r'\w{6,15}'
result = re.match(template, password, flags=re.ASCII)

print("Thank you!") if result else print("Error!")
