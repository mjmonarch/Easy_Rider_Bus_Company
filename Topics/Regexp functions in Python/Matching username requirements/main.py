import re

template = "[a-z]"
str_input = input()

result = re.match(template, str_input, flags=re.IGNORECASE)
print("Thank you!") if result else print("Oops! The username has to start with a letter.")
